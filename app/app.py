import streamlit as st
import pandas as pd
import pickle
import time
import random
import numpy as np
import os

# --- 1. SAYFA KONFİGÜRASYONU VE TEMALANDIRMA ---
st.set_page_config(page_title="International Match Predictor AI", page_icon="🏆", layout="centered")

def set_bg_and_style():
    st.markdown(f"""
    <style>
    .stApp {{ background: linear-gradient(135deg, #001338 0%, #000814 100%); background-attachment: fixed; color: white; }}
    .stSelectbox div[data-baseweb="select"] {{ background-color: rgba(0, 31, 63, 0.6); border: 1px solid #00f2ff; border-radius: 10px; color: white; }}
    div[data-testid="stThumbValue"] {{ color: #00ffcc !important; font-weight: bold; }}
    .stButton>button {{ width: 100%; background: linear-gradient(90deg, #00f2ff, #7000ff); border: none; color: white; padding: 15px 32px; font-size: 20px; font-weight: bold; border-radius: 50px; box-shadow: 0 0 15px rgba(0, 242, 255, 0.4); transition: 0.4s; }}
    .stButton>button:hover {{ box-shadow: 0 0 30px rgba(112, 0, 255, 0.8); transform: scale(1.02); }}
    @keyframes kickBall {{ 0% {{ transform: translate(-100px, 0) rotate(0deg); opacity: 0; }} 20% {{ opacity: 1; }} 100% {{ transform: translate(300px, -80px) rotate(720deg); opacity: 0; }} }}
    .soccer-ball {{ font-size: 40px; position: absolute; z-index: 1000; display: none; }}
    .animate-kick {{ display: block !important; animation: kickBall 1s forwards cubic-bezier(0.17, 0.67, 0.83, 0.67); }}
    @keyframes dropDown {{ 0% {{ transform: translateY(-50px) rotate(-2deg); opacity: 0; }} 100% {{ transform: translateY(0) rotate(0deg); opacity: 1; }} }}
    @keyframes ledBlink {{ 0%, 100% {{ text-shadow: 0 0 10px #deff9a, 0 0 20px #deff9a; }} 50% {{ text-shadow: 0 0 2px #deff9a; opacity: 0.9; }} }}
    .vip-ticket {{ background: linear-gradient(135deg, rgba(0, 19, 56, 0.9), rgba(112, 0, 255, 0.4)); border: 2px dashed #00f2ff; border-radius: 15px; padding: 30px; margin-top: 20px; position: relative; animation: dropDown 1s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards; box-shadow: 0 20px 40px rgba(0,0,0,0.5), inset 0 0 20px rgba(0, 242, 255, 0.2); display: flex; justify-content: space-between; align-items: center; }}
    .vip-ticket::before {{ content: ''; position: absolute; left: -15px; top: 50%; transform: translateY(-50%); width: 30px; height: 30px; background-color: #000814; border-radius: 50%; border-right: 2px dashed #00f2ff; }}
    .vip-ticket::after {{ content: ''; position: absolute; right: -15px; top: 50%; transform: translateY(-50%); width: 30px; height: 30px; background-color: #000814; border-radius: 50%; border-left: 2px dashed #00f2ff; }}
    .led-text {{ font-family: 'Courier New', monospace; color: #deff9a; font-size: 2.2rem; font-weight: 900; letter-spacing: 2px; text-transform: uppercase; animation: ledBlink 1.5s infinite; }}
    .barcode {{ font-family: 'Courier New', monospace; font-size: 10px; color: rgba(255,255,255,0.4); writing-mode: vertical-rl; letter-spacing: -2px; }}
    </style>
    """, unsafe_allow_html=True)

set_bg_and_style()

# --- DİNAMİK DOSYA YOLU BULUCU ---
# Bu kod app.py nereden çalıştırılırsa çalıştırılsın 'models' klasörünü kusursuz bulur.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, '../models/champion_xgboost_model.pkl')
ENCODERS_PATH = os.path.join(BASE_DIR, '../models/label_encoders.pkl')

# --- 2. MODEL YÜKLEME ---
@st.cache_resource 
def load_assets():
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    with open(ENCODERS_PATH, 'rb') as f:
        encoders = pickle.load(f)
    return model, encoders

try:
    model, encoders = load_assets()
except Exception as e:
    st.error(f"🚨 Model dosyaları bulunamadı! Lütfen '../models' klasöründe pkl dosyalarının olduğundan emin olun.")
    st.warning(f"Sistem Hatası: {e}")
    st.stop() # EĞER DOSYALAR YOKSA KOD BURADA DURUR, AŞAĞIYA İNİP ÇÖKMEZ.

# --- MANTIK VE COĞRAFYA KALKANI ---
def check_match_logic(home, away, tourney, match_country, neutral):
    if home == away:
        return False, "⚠️ Kural İhlali: Ev sahibi ve deplasman takımları aynı olamaz!"
    
    # 1. PARADOKS ÇÖZÜCÜ: Tarafsız saha ise, oynanan ülke takımlardan biri olamaz!
    if neutral and (home == match_country or away == match_country):
        return False, f"🛑 Mantık Hatası: Tarafsız saha (Neutral) seçiliyken maçın oynandığı ülke ({match_country}) takımlardan biri olamaz! Lütfen ülkeyi 'Qatar', 'Germany' gibi 3. bir ülke yapın."

    # 2. Ev sahibi - Ülke kuralı
    if not neutral and home != match_country:
        return False, f"🛑 Mantık Hatası: Maç '{match_country}' ülkesinde oynanıyorsa ve tarafsız değilse, Ev Sahibi takım '{match_country}' olmalıdır."
    
    south_america = ["Argentina", "Brazil", "Uruguay", "Colombia", "Chile", "Peru", "Ecuador", "Paraguay", "Bolivia", "Venezuela"]
    europe = ["Turkey", "Germany", "France", "Italy", "Spain", "England", "Portugal", "Netherlands", "Belgium", "Croatia", "Switzerland"]
    euro_tournaments = ["UEFA Euro", "UEFA Nations League", "European Nations League", "UEFA Euro qualification"]
    copa_tournaments = ["Copa America"]
    
    if tourney in euro_tournaments:
        if home in south_america or away in south_america:
            return False, f"🛑 Coğrafya Hatası: {tourney} turnuvasında Güney Amerika takımları oynayamaz!"
            
    if tourney in copa_tournaments:
        if home in europe or away in europe:
            return False, f"🛑 Coğrafya Hatası: {tourney} turnuvasında Avrupa takımları oynayamaz!"
            
    return True, ""

# --- 3. ARAYÜZ ---
st.title("🏆International Match Predictor AI")
st.write("---")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🏰 Ev Sahibi")
    home_team = st.selectbox("Takım Seçin", encoders['home_team'].classes_, key="h1")
    home_form = st.slider("Form Gücü", 0.0, 1.0, 0.6, 0.1)

with col2:
    st.markdown("### ✈️ Deplasman")
    away_team = st.selectbox("Takım Seçin", encoders['away_team'].classes_, key="a1")
    away_form = st.slider("Form Gücü", 0.0, 1.0, 0.4, 0.1)

c1, c2 = st.columns(2)
with c1:
    tournament = st.selectbox("Turnuva", encoders['tournament'].classes_)
    match_year = st.number_input("Yıl", 2024, 2030, 2026)
with c2:
    country = st.selectbox("Mekan", encoders['country'].classes_)
    is_neutral = st.toggle("Tarafsız Saha", value=False)

st.write("---")

# --- 4. TAHMİN ---
ball_placeholder = st.empty()

if st.button("⚽ ANALİZİ BAŞLAT VE ŞUT ÇEK!"):
    
    is_valid, error_msg = check_match_logic(home_team, away_team, tournament, country, is_neutral)
    if not is_valid:
        st.error(error_msg)
        st.stop()
        
    ball_placeholder.markdown('<div class="soccer-ball animate-kick">⚽</div>', unsafe_allow_html=True)
    
    st.markdown("#### ⚙️ Yapay Zeka Taktik Simülasyonu Çalışıyor...")
    progress_bar = st.progress(50)
    status_text = st.empty()
    
    for i in range(15):
        val = random.randint(30, 70)
        progress_bar.progress(val)
        status_text.caption(f"Deplasman Baskısı %{100-val} | Ev Sahibi Baskısı %{val}")
        time.sleep(0.15)
        
    try:
        encoded_home = encoders['home_team'].transform([home_team])[0]
        encoded_away = encoders['away_team'].transform([away_team])[0]
        encoded_tournament = encoders['tournament'].transform([tournament])[0]
        encoded_country = encoders['country'].transform([country])[0]
        
        input_std = pd.DataFrame([[
            encoded_home, encoded_away, encoded_tournament, encoded_country, 
            1 if is_neutral else 0, match_year, home_form, away_form
        ]], columns=['home_team', 'away_team', 'tournament', 'country', 'neutral', 'year', 'home_team_form', 'away_team_form'])
        
        # --- TTA (ÇİFT YÖNLÜ ÇAPRAZLAMA) ---
        if is_neutral:
            input_flipped = pd.DataFrame([[
                encoded_away, encoded_home, encoded_tournament, encoded_country, 
                1, match_year, away_form, home_form
            ]], columns=['home_team', 'away_team', 'tournament', 'country', 'neutral', 'year', 'home_team_form', 'away_team_form'])
            
            prob_std = model.predict_proba(input_std)[0]     
            prob_flipped = model.predict_proba(input_flipped)[0] 
            
            avg_draw = (prob_std[0] + prob_flipped[0]) / 2
            avg_home_wins = (prob_std[2] + prob_flipped[1]) / 2 
            avg_away_wins = (prob_std[1] + prob_flipped[2]) / 2 
        else:
            prob_std = model.predict_proba(input_std)[0]
            avg_draw, avg_away_wins, avg_home_wins = prob_std[0], prob_std[1], prob_std[2]
            
        # --- DİNAMİK FORM ETKİSİ (Yükseltildi) ---
        form_diff = home_form - away_form
        form_impact = form_diff * 0.15  # Form etkisi %15'e çıkarıldı!
        
        avg_home_wins += form_impact
        avg_away_wins -= form_impact
        
        # Sınırlandırma ve %100'e (1.0) Eşitleme
        avg_home_wins = max(0.01, avg_home_wins)
        avg_away_wins = max(0.01, avg_away_wins)
        avg_draw = max(0.01, avg_draw)
        
        total = avg_home_wins + avg_away_wins + avg_draw
        
        home_prob = (avg_home_wins / total) * 100
        away_prob = (avg_away_wins / total) * 100
        draw_prob = (avg_draw / total) * 100
        
        probabilities = [draw_prob, away_prob, home_prob]
        res_idx = int(np.argmax(probabilities))
        confidence_score = probabilities[res_idx] # Tüm oranlar artık tamamen senkronize!
        
        # Animasyon Barını Kilitleme
        if res_idx == 0: progress_bar.progress(50)
        elif res_idx == 1: progress_bar.progress(int(100 - confidence_score))
        else: progress_bar.progress(int(confidence_score))
        status_text.empty()
        
        mapping = { 0: "MAÇ BERABERE", 1: f"{away_team} KAZANIR", 2: f"{home_team} KAZANIR" }
        
        st.markdown(f"""
<div class="vip-ticket">
<div style="flex-grow: 1; width: 100%;">
<p style="color: #00f2ff; margin:0; font-size: 14px; text-transform: uppercase;">Resmi Tahmin Sonucu</p>
<div class="led-text">{mapping[res_idx]}</div>

<div style="display: flex; justify-content: space-between; margin-top: 20px; margin-bottom: 15px; background: rgba(0, 8, 20, 0.6); padding: 15px; border-radius: 10px; border: 1px solid rgba(0, 242, 255, 0.2);">
<div style="text-align: center; width: 30%;">
<div style="font-size: 12px; color: #aaa;">🏠 {home_team}</div>
<div style="font-size: 20px; color: #deff9a; font-weight: bold;">%{home_prob:.1f}</div>
</div>
<div style="text-align: center; border-left: 1px solid rgba(255,255,255,0.1); border-right: 1px solid rgba(255,255,255,0.1); width: 33%;">
<div style="font-size: 12px; color: #aaa;">🤝 Beraberlik</div>
<div style="font-size: 20px; color: #deff9a; font-weight: bold;">%{draw_prob:.1f}</div>
</div>
<div style="text-align: center; width: 30%;">
<div style="font-size: 12px; color: #aaa;">✈️ {away_team}</div>
<div style="font-size: 20px; color: #deff9a; font-weight: bold;">%{away_prob:.1f}</div>
</div>
</div>

<p style="color: rgba(255,255,255,0.4); margin:0; font-size: 11px;">* Yapay Zeka (TTA) ve Dinamik Form Algoritması ile senkronize edilmiştir.</p>
</div>
<div class="barcode">||| || | || | | || | | || | | |||</div>
</div>
""", unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Sistem Hatası: {e}")
        
    time.sleep(1.5)
    ball_placeholder.empty()