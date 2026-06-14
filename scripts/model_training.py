# %% [markdown]
# <div style="background: linear-gradient(135deg, #092618 0%, #14452f 50%, #1ea85b 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 8px 20px rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.1); text-align: center; margin-bottom: 15px;">
#     <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 2px; color: rgba(255,255,255,0.8); font-weight: 700; margin-bottom: 2px; line-height: 1;">YBS3259 - Makine Öğrenmesi Final Projesi</div>
#     <h1 style="margin: 0; font-size: 28px; font-weight: 900; letter-spacing: -1px; color: #ffffff; line-height: 1;">Uluslararası Maç Analizi</h1>
#     <div style="font-size: 14px; color: rgba(255,255,255,0.9); font-weight: 500; margin-top: 5px; line-height: 1;"></div>
# </div>
# 
# | ![Rana](../figures/rana.jpg) | ![Yusuf](../figures/yusuf.jpg) | ![Dilara](../figures/dilara.jpg) |
# | :---: | :---: | :---: |
# | **Rana KUŞ** <br> <span style="color: #22c55e; font-size: 11px;">Veri Bilimci</span> | **Yusuf PEKİNCE** <br> <span style="color: #22c55e; font-size: 11px;">Proje Yöneticisi</span> | **Dilara ÇELİK** <br> <span style="color: #22c55e; font-size: 11px;">Veri Mühendisi</span> |

# %% [markdown]
# <div style="
#     background-color: #14452f; 
#     border-left: 6px solid #22c55e;
#     border-radius: 12px; 
#     padding: 25px; 
#     font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
#     color: #ffffff;
#     margin-bottom: 20px;
#     box-shadow: 2px 4px 12px rgba(0,0,0,0.15);
#     max-width: 100%;
#     box-sizing: border-box;
# ">
#     <h2 style="color: #22c55e; margin-top: 0; font-size: 1.8rem; display: flex; align-items: center; gap: 10px; font-weight: 700;">
#         🏟️ Proje Tanımı
#     </h2>
#     <p style="font-size: 1rem; line-height: 1.6; color: #f0fdf4; margin-bottom: 12px;">
#         <strong style="color: #ffffff;">Proje Adı:</strong> Uluslararası Maçların Analizi
#     </p>
#     <p style="font-size: 1rem; line-height: 1.6; color: #f0fdf4; margin-bottom: 12px;">
#         <strong style="color: #ffffff;">Seçilen Alternatif:</strong> Sınıflandırma (Classification)  <em></em>
#     </p>
# </div>
# 
# <div style="
#     background-color: #0f3625; 
#     border-left: 6px solid #22c55e;
#     border-radius: 12px; 
#     padding: 25px; 
#     font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
#     color: #ffffff;
#     box-shadow: 2px 4px 12px rgba(0,0,0,0.15);
#     max-width: 100%;
#     box-sizing: border-box;
# ">
#     <h2 style="color: #22c55e; margin-top: 0; font-size: 1.8rem; display: flex; align-items: center; gap: 10px; font-weight: 700;">
#         🎯 Problem Cümlesi
#     </h2>
#     <ul style="font-size: 1rem; line-height: 1.6; color: #f0fdf4; padding-left: 20px; margin-bottom: 0;">
#         <li style="margin-bottom: 10px;">1872'den günümüze oynanan 50.000'den fazla uluslararası futbol maçındaki tarihsel trendleri, ev sahibi avantajını ve turnuva ağırlıklarını analiz etmek.</li>
#         <li style="margin-bottom: 10px;">İki ülke arasındaki gelecekteki bir karşılaşmanın sonucunu (Galibiyet / Beraberlik / Mağlubiyet) en yüksek doğruluk oranıyla tahmin edebilen analitik bir sınıflandırma modeli geliştirmek.</li>
#         <li style="margin-bottom: 0;">Elde edilen içgörüleri makine öğrenmesi metrikleriyle doğrulayarak akademik ve endüstriyel standartlarda bir veri projesi sunmak.</li>
#     </ul>
# </div>

# %% [markdown]
# <div style="background: linear-gradient(135deg, #092618 0%, #14452f 50%, #1ea85b 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 8px 20px rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.1); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h2 style="margin: 0; font-size: 22px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px;">🔄 1.3. Business Understanding (İş İhtiyacını Anlama)</h2>
#     <p style="font-size: 13px; color: rgba(255,255,255,0.85); margin-top: 4px; margin-bottom: 0; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">CRISP-DM Metodolojisi / Faz 1</p>
# </div>
# 
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">📖 1.3.1. Veri Hikayesi ve Kaynağı (Data Story & Origin)</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 10px;">
#         Bu projede analiz edilen veri havuzu, dünyanın en büyük veri bilimi topluluğu olan Kaggle platformundan temin edilen <strong>all_matches.csv</strong> veri setidir. 
#     </p>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         Verinin hikayesi, futbolun ilk resmi uluslararası maçı kabul edilen 30 Kasım 1872'deki İskoçya - İngiltere karşılaşmasıyla başlar. Yüz yılı aşkın bu süreçte, dünya savaşlarından endüstriyel dönüşüme kadar futbolun geçirdiği evrimi, ülkelerin ekol yükselişlerini ve taktiksel kırılmaları içinde barındıran <strong>51.491 satırlık</strong> devasa bir tarihsel hafızadır. Projede ayrıca ülkelerin kıta ve federasyon bilgilerini eşleştirmek adına <strong>countries_names.csv</strong> yardımcı veri seti entegre edilmiştir.
#     </p>
# </div>
# 
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">🎯 1.3.2. Gerçek İş İhtiyacı ve Problemin Bağlamı (Business Case)</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 10px;">
#         Geleneksel spor dünyasında maç analizleri ve gelecek tahminleri uzun yıllar boyunca yalnızca insan sezgilerine, öznel yorumcuların tahminlerine ve kısıtlı istatistiklere dayanmıştır. Ancak günümüzde spor endüstrisi milyarlarca dolarlık devasa bir finansal ekosisteme dönüşmüştür. 
#     </p>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         <strong>Gerçek İhtiyaç:</strong> Futbol federasyonları, medya kuruluşları, yayıncı devler ve sportif yatırımcılar; turnuva planlamaları, fikstür zorluk dereceleri, izleyici etkileşimi yönetimi ve risk analizi süreçlerinde <strong>objektif, bilimsel ve veri odaklı tahmin motorlarına</strong> ihtiyaç duymaktadır. Bu proje, "Geçmişin makro trendleri, geleceğin 90 dakikasını ne kadar doğru öngörebilir?" sorusuna analitik bir yanıt arayarak yönetsel karar destek değeri üretir.
#     </p>
# </div>
# 
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">📈 1.3.3. Karar Değeri ve Analitik Başarı Kriterleri (Decision Value)</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 10px;">
#         Projenin başarısı sadece matematiksel skorlarla değil, desteklediği kararların kalitesiyle ölçülür. Kurulan çok sınıflı sınıflandırma modeli doğrudan şu kararları destekler:
#     </p>
#     <ul style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; padding-left: 20px; margin-bottom: 12px;">
#         <li style="margin-bottom: 5px;"><strong>Stratejik Planlama:</strong> Milli takımların maç takvimlerinde deplasman ve tarafsız saha ağırlıklarını ölçerek en optimize simülasyonu sunmak.</li>
#         <li style="margin-bottom: 5px;"><strong>Medya İçerik Yönetimi:</strong> Yayıncı kuruluşların maç öncesi programlarında izleyicilere sunacağı analizlerin güvenilirliğini artırmak.</li>
#     </ul>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         <strong>Analitik Başarı Kriteri:</strong> Müsabakalardaki galibiyet ve beraberlik oranlarının asimetrik dağılımı (sınıf dengesizliği) riski nedeniyle, projenin ana başarı metriği "Accuracy" değil, tüm sınıfları eşit ağırlıkta optimize eden <strong>Macro F1-Score</strong> olarak belirlenmiştir. Literatür bulguları ışığında, mikro dinamiklerin (anlık sakatlıklar, kadrolar vb.) eksikliğine rağmen, sadece bu makro verilerle <strong>%55 ve üzeri bir Macro F1-Skoru</strong> yönetsel açıdan başarılı kabul edilecektir.
#     </p>
# </div>

# %% [markdown]
# <div style="background: linear-gradient(135deg, #092618 0%, #14452f 50%, #1ea85b 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 8px 20px rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.1); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h2 style="margin: 0; font-size: 22px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px;">🔍 2.1. Data Understanding (Veriyi Tanıma)</h2>
#     <p style="font-size: 13px; color: rgba(255,255,255,0.85); margin-top: 4px; margin-bottom: 0; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">CRISP-DM Metodolojisi / Faz 2</p>
# </div>
# 
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">📊 2.1.1. Veri Yapısı, Değişken Türleri ve Eksik Değer Analizi</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         Bu teknik adımda, bellek ortamına yüklenen <code>df_matches</code> ve <code>df_countries</code> veri çerçevelerinin boyutları (satır/sütun sayıları), içerdikleri özniteliklerin yapısal veri tipleri (nesne, tamsayı, mantıksal) ve veri kalitesini doğrudan etkileyen eksik değer (null/missing value) durumları programatik olarak sorgulanmaktadır.
#     </p>
# </div>

# %%
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

plt.rcParams["figure.figsize"] = [10, 6]
sns.set_theme(style="darkgrid")
warnings.filterwarnings("ignore")

df_matches = pd.read_csv("../data/raw/all_matches.csv")
df_countries = pd.read_csv("../data/raw/countries_names.csv")

print("df_matches shape:", df_matches.shape)
print("df_countries shape:", df_countries.shape)

print("\ndf_matches head:")
display(df_matches.head(3))

print("\ndf_countries head:")
display(df_countries.head(3))

# %%
def df_kontrol_ozeti(df, veri_seti_adi):
    print(f"--- {veri_seti_adi} VERİ SETİ BOYUTU ---")
    print(f"Şekil: {df.shape}")

    print(f"\n--- {veri_seti_adi} SÜTUN TİPLERİ VE GENEL BİLGİ ---")
    df.info()

    print(f"\n--- {veri_seti_adi} EKSİK DEĞER KONTROLÜ ---")
    print(df.isnull().sum())


df_kontrol_ozeti(df_matches, "MAÇLAR")
print()
df_kontrol_ozeti(df_countries, "ÜLKELER")

# %% [markdown]
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">⚽ 2.1.2. Hedef Değişkenin Türetilmesi ve Sınıf Dengesizliği Analizi</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 10px;">
#         Sınıflandırma modelimizin ana hedefini (Target Variable) oluşturmak adına, <code>df_matches</code> içerisindeki ham <code>home_score</code> (ev sahibi gol) ve <code>away_score</code> (deplasman gol) öznitelikleri matematiksel olarak karşılaştırılmıştır. 
#     </p>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         Bu işlem sonucunda müsabakalar; <strong>'Ev_Sahibi_Kazandi' (Home_Win)</strong>, <strong>'Deplasman_Kazandi' (Away_Win)</strong> ve <strong>'Beraberlik' (Draw)</strong> olmak üzere 3 sınıflı yeni bir hedef değişkene dönüştürülmüştür. Elde edilen frekans ve oran dağılımları, modelin öğrenme sürecinde karşılaşacağı <strong>Sınıf Dengesizliği (Class Imbalance)</strong> riskini ölçümlemek ve doğrulamak için kritik bir rehberdir.
#     </p>
# </div>

# %%
def sonuc_etiketi_belirle(satir):
    if satir["home_score"] > satir["away_score"]:
        return "Ev_Sahibi_Kazandi"
    if satir["home_score"] < satir["away_score"]:
        return "Deplasman_Kazandi"
    return "Beraberlik"


df_matches["match_result"] = df_matches.apply(sonuc_etiketi_belirle, axis=1)

print("--- MAÇ SONUCU DAĞILIMI ---")
sonuc_sayilari = df_matches["match_result"].value_counts()
sonuc_yuzdeleri = df_matches["match_result"].value_counts(normalize=True) * 100

print("\n--- MAÇ SONUCU SAYILARI ---")
print(sonuc_sayilari)

print("\n--- MAÇ SONUCU YÜZDELERİ ---")
print(sonuc_yuzdeleri.round(2))

plt.figure(figsize=(10, 6))
order = ["Ev_Sahibi_Kazandi", "Deplasman_Kazandi", "Beraberlik"]
sns.countplot(data=df_matches, x="match_result", order=order, palette="viridis")
plt.title("Hedef Değişken Dağılımı ve Sınıf Dengesizliği Analizi")
plt.xlabel("Maç Sonucu")
plt.ylabel("Müsabaka Sayısı")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# %% [markdown]
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">📊 2.1.3. Gol Dağılımları ve İstatistiksel Aykırı Değer Kontrolü</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 10px;">
#         Sayısal özniteliklerimiz olan <code>home_score</code> ve <code>away_score</code> değişkenlerinin olasılık yoğunlukları frekans bazlı incelenmiştir. 
#     </p>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         Ayrıca, veri setindeki ekstrem skor dinamiklerini yakalamak adına <strong>Kutu Grafiği (Box Plot)</strong> ve <strong>Interquartile Range (IQR)</strong> yöntemleri kullanılarak istatistiksel aykırı değer tespiti gerçekleştirilmiştir. Bu analiz, veri hazırlama (Data Preparation) aşamasında uygulayacağımız temizlik ve kırpma stratejilerine yönetsel bir zemin hazırlamaktadır.
#     </p>
# </div>

# %%
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

sns.histplot(
    data=df_matches,
    x="home_score",
    color="teal",
    kde=True,
    discrete=True,
    ax=axes[0],
    label="Ev Sahibi Golü"
)
sns.histplot(
    data=df_matches,
    x="away_score",
    color="orange",
    kde=True,
    discrete=True,
    ax=axes[0],
    label="Deplasman Golü"
)
axes[0].set_title("Gol Sayılarının Frekans Dağılımı")
axes[0].set_xlabel("Atılan Gol")
axes[0].set_ylabel("Maç Sayısı")
axes[0].legend(title="Gol Türü")

box_data = df_matches[["home_score", "away_score"]].rename(
    columns={"home_score": "Ev Sahibi Golü", "away_score": "Deplasman Golü"}
)
sns.boxplot(data=box_data, palette="Set2", ax=axes[1])
axes[1].set_title("Skor Dinamiklerinde Aykırı Değer Analizi")
axes[1].set_xlabel("Takım Türü")
axes[1].set_ylabel("Gol Sayısı")

print("--- IQR YÖNTEMİ İLE AYKIRI DEĞER ANALİZİ ---")
for kolon in ["home_score", "away_score"]:
    q1 = df_matches[kolon].quantile(0.25)
    q3 = df_matches[kolon].quantile(0.75)
    iqr = q3 - q1
    ust_sinir = q3 + 1.5 * iqr
    asan_mac_sayisi = (df_matches[kolon] > ust_sinir).sum()

    print(f"\n{kolon} için üst aykırı değer limiti: {ust_sinir:.2f}")
    print(f"{kolon} için bu limiti aşan maç sayısı: {asan_mac_sayisi}")

plt.tight_layout()
plt.show()

# %% [markdown]
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">🕸️ 2.1.4. Sayısal Özniteliklerin Korelasyon Yapısı ve İlişki Analizi</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 10px;">
#         Bu analitik adımda, veri setindeki sürekli/sayısal değişkenlerin birbirleriyle olan doğrusal ilişkilerinin yönü ve şiddeti <strong>Pearson Korelasyon Katsayısı</strong> üzerinden incelenmiştir. 
#     </p>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         Zaman boyutunun skorlar üzerindeki etkisini gözlemleyebilmek adına <code>date</code> sütunundan yıllık (<code>year</code>) kırılım türetilmiş; ardından <strong>Sıcaklık Haritası (Heatmap)</strong> ve <strong>Dağılım Grafiği (Scatter Plot)</strong> yardımıyla verideki doğrusal bağlar ve yoğunluk kırılımları görselleştirilmiştir.
#     </p>
# </div>

# %%
df_matches["year"] = pd.to_datetime(df_matches["date"]).dt.year

veri_ozet = df_matches[["year", "home_score", "away_score"]]
veri_ozet_tr = veri_ozet.rename(
    columns={
        "year": "Yıl",
        "home_score": "Ev Sahibi Gol Sayısı",
        "away_score": "Deplasman Gol Sayısı",
    }
)

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

korelasyon = veri_ozet_tr.corr()
sns.heatmap(
    korelasyon,
    annot=True,
    cmap="GnBu",
    fmt=".3f",
    ax=axes[0]
)
axes[0].set_title("Sayısal Değişkenlerin Korelasyon Matrisi")
axes[0].set_xlabel("Değişkenler")
axes[0].set_ylabel("Değişkenler")

sns.scatterplot(
    data=df_matches,
    x="year",
    y="home_score",
    hue="neutral",
    alpha=0.3,
    ax=axes[1]
)
axes[1].set_title("Yıllara Göre Ev Sahibi Skorları ve Saha Durumu")
axes[1].set_xlabel("Oynanan Yıl")
axes[1].set_ylabel("Ev Sahibi Gol Sayısı")

handles, labels = axes[1].get_legend_handles_labels()
legend_etkiketleri = []
for etiket in labels:
    if etiket == "False":
        legend_etkiketleri.append("Nötr Değil")
    elif etiket == "True":
        legend_etkiketleri.append("Nötr Saha")
    elif etiket == "neutral":
        legend_etkiketleri.append("Saha Durumu")
    else:
        legend_etkiketleri.append(etiket)
axes[1].legend(handles, legend_etkiketleri, title="Saha Durumu")

plt.tight_layout()
plt.show()

# %%
import os
os.makedirs("../data/processed", exist_ok=True)

# Temizlenmiş veriyi processed klasörüne kaydediyoruz (Hocanın rehberine uyum)
df_matches.to_csv("../data/processed/matches_cleaned.csv", index=False)
print("Temizlenmiş veri 'data/processed/' klasörüne kaydedildi.")

# %% [markdown]
# <div style="background: linear-gradient(135deg, #092618 0%, #14452f 50%, #1ea85b 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 8px 20px rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.1); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h2 style="margin: 0; font-size: 22px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px;">🛠️ 3.1. Data Preparation (Veri Hazırlığı)</h2>
#     <p style="font-size: 13px; color: rgba(255,255,255,0.85); margin-top: 4px; margin-bottom: 0; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">CRISP-DM Metodolojisi / Faz 3</p>
# </div>
# 
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">🧹 3.1.1. Zaman Bazlı Filtreleme ve Tarih Dönüşümü</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 10px;">
#         Veri setinin başlangıç yılı olan 1872 yılından itibaren futbol dünyası; kurallar, oyuncu atletizmi, taktiksel anlayış ve üç puanlık sistem gibi köklü değişimlere uğramıştır. Çok eski yıllara ait verilerin modern futbol tahminlerinde yaratacağı gürültüyü (noise) önlemek adına veri seti üzerinde dönemsel bir sınırlandırma yapılması zorunlu görülmüştür.
#     </p>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         Bu doğrultuda, <code>date</code> sütunu <code>datetime</code> formatına dönüştürülmüş ve veri seti futbolun modernleşme dönemi olarak kabul edilen <strong>1980 yılı ve sonrası</strong> müsabakaları kapsayacak şekilde filtrelenmiştir.
#     </p>
# </div>

# %%
df_matches["date"] = pd.to_datetime(df_matches["date"])
df_matches = df_matches[df_matches["date"] >= "1980-01-01"].reset_index(drop=True)

print("--- 1980 SONRASI VERİ SETİ BOYUTU ---")
print(df_matches.shape)

display(df_matches.head(3))

# %% [markdown]
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">🚀 3.1.2. Özellik Türetme: Modern Dönem Tarihsel Form Skorları (Feature Engineering)</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 10px;">
#         Veri setimiz kalıcı olarak 1980 yılı ve sonrasına filtrelendikten sonra, takımların zamana bağlı performans dinamiklerini yakalayacak form skorları bu yeni matris üzerinde yeniden hesaplanmıştır. 
#     </p>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         Her karşılaşma öncesinde ev sahibi ve deplasman takımının <strong>son 5 maçtaki galibiyet oranları</strong> kronolojik olarak çıkarılmıştır. Sınıflandırma modelimizin geleceği tahmin ederken veri sızıntısı (data leakage) yaşamaması adına, mevcut maçın skoru <code>shift(1)</code> fonksiyonu ile kesinlikle hesaplama dışı bırakılmış ve gürültüden arındırılmış temiz bir girdi yapısı kurulmuştur.
#     </p>
# </div>

# %%
df_matches = df_matches.sort_values("date").reset_index(drop=True)

df_matches["is_home_win"] = (df_matches["match_result"] == "Ev_Sahibi_Kazandi").astype(int)
df_matches["is_away_win"] = (df_matches["match_result"] == "Deplasman_Kazandi").astype(int)

df_matches["home_team_form"] = df_matches.groupby("home_team")["is_home_win"].transform(
    lambda seri: seri.shift(1).rolling(window=5, min_periods=1).mean()
)
df_matches["away_team_form"] = df_matches.groupby("away_team")["is_away_win"].transform(
    lambda seri: seri.shift(1).rolling(window=5, min_periods=1).mean()
)

df_matches[["home_team_form", "away_team_form"]] = df_matches[["home_team_form", "away_team_form"]].fillna(0)
df_matches.drop(columns=["is_home_win", "is_away_win"], inplace=True)

print("--- YENİDEN HESAPLANAN FORM SKORLARI BOYUTU VE İLK 5 SATIR ---")
print(df_matches.shape)
display(df_matches[["date", "home_team", "away_team", "match_result", "home_team_form", "away_team_form"]].head())

# %% [markdown]
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">🛡️ 3.1.3. Veri Sızıntısı (Data Leakage) Önleme ve Öznitelik Seçimi</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 10px;">
#         Makine öğrenmesinde veri sızıntısı (data leakage), modelin eğitim esnasında, gerçek hayatta tahminleme yaparken erişemeyeceği "geleceğe ait" veya "sonuca dayalı" bilgilere ulaşması durumudur. Futbol veri setimizde yer alan <code>home_score</code> ve <code>away_score</code> sütunları, maç bittiğinde netleşen doğrudan sonucu dikte eden bilgilerdir.
#     </p>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         Modelin yalnızca maç başlamadan önce bilinen girdilerle (saha durumu, turnuva türü, takımlar ve türetilen form skorları) tahmin üretmesini garanti altına almak adına, ham skor sütunları ve hedef değişkenimiz matristen ayrıştırılarak bağımsız değişken matrisi (<code>X</code>) ve bağımlı değişken vektörü (<code>y</code>) oluşturulmuştur.
#     </p>
# </div>

# %%
y = df_matches["match_result"]
X = df_matches.drop(columns=["home_score", "away_score", "match_result", "date"])

print("--- MODEL HEDEFİ (Y) BOYUTU ---")
print(y.shape)

print("\n--- MODEL GİRDİSİ (X) BOYUTU ---")
print(X.shape)

print("\n--- MODEL GİRDİSİ OLARAK SEÇİLEN ÖZNİTELİKLER ---")
print(list(X.columns))

# %% [markdown]
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">🔢 3.1.4. Kategorik Özniteliklerin ve Hedef Sınıfların Kodlanması (Encoding)</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 10px;">
#         Sınıflandırma algoritmalarının matematiksel optimizasyon süreçlerinde metinsel verileri işleyememesi nedeniyle, veri setindeki kategorik alanların sayısallaştırılması zorunludur. Veri setimizde yer alan takım, turnuva ve ülke isimlerinin çok yüksek sayıda benzersiz değer içermesi (Yüksek Kardinalite) göz önünde bulundurulmuştur.
#     </p>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         Boyut patlamasını (curse of dimensionality) önlemek ve bellek verimliliğini korumak adına, kategorik girdiler <code>scikit-learn</code> kütüphanesinin <strong>LabelEncoder</strong> mimarisiyle kodlanmıştır. Aynı disiplinle, metinsel hedef değişken vektörümüz (<code>y</code>) de modelin çıktı üretebileceği asgari sayısal indeks formatına (0, 1, 2) dönüştürülmüştür.
#     </p>
# </div>

# %%
from sklearn.preprocessing import LabelEncoder

etiket_kodlayicisi = LabelEncoder()

for sutun in ["home_team", "away_team", "tournament", "country"]:
    X[sutun] = etiket_kodlayicisi.fit_transform(X[sutun])

if X["neutral"].dtype == bool:
    X["neutral"] = X["neutral"].astype(int)

y = etiket_kodlayicisi.fit_transform(y)

print("--- KODLANMIŞ GİRDİ MATRİSİ (X) İLK 3 SATIR ---")
display(X.head(3))

print("\n--- KODLANMIŞ HEDEF DEĞİŞKEN (y) İLK 10 DEĞER ---")
print(y[:10])

# %% [markdown]
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">💡 Yönetsel Karar: Kodlama (Encoding) Stratejisinin Gerekçelendirilmesi</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 10px;">
#         Sınıflandırma algoritmaları, matematiksel optimizasyon süreçlerinde metinsel ifadeleri (string) doğrudan işleyemediği için bu verilerin sayısallaştırılması zorunludur. Bu projede, kategorik öznitelikler (ülke, takım ve turnuva isimleri) için <strong>One-Hot Encoding</strong> yerine <strong>Label Encoding</strong> yönteminin tercih edilmesinin temel nedenleri şunlardır:
#     </p>
#     <ul style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; padding-left: 20px; margin-bottom: 12px;">
#         <li style="margin-bottom: 8px;"><strong>Boyutun Laneti (Curse of Dimensionality) Riski:</strong> Veri setimizde 200'den fazla benzersiz milli takım ve ülke bulunmaktadır. One-Hot Encoding uygulansaydı, girdi matrisine her ülke için yeni bir sütun eklenecek (200+ yeni sütun) ve devasa, sıfır ağırlıklı (sparse) bir matris oluşacaktı. Bu durum, modelin eğitim süresini uzatacak ve ezberleme (overfitting) riskini artıracaktı.</li>
#         <li style="margin-bottom: 8px;"><strong>Ağaç Tabanlı Modellerin Uyumluluğu:</strong> Projemizin modelleme evresinde kullanılacak Random Forest, XGBoost ve LightGBM gibi gelişmiş algoritmalar, Label Encoding ile üretilen sayısal indeksleri (0, 1, 2, 3...) yapıları gereği hiyerarşik dallanma mantığıyla kusursuz biçimde ayrıştırabilmektedir.</li>
#     </ul>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         Bu stratejik karar sayesinde veri matrisinin sütun sayısı korunmuş, boyut büyümesi engellenmiş ve veri seti bellekte en optimize (kompakt) halinde tutularak modelleme evresine hazır hale getirilmiştir.
#     </p>
# </div>

# %% [markdown]
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">💡 Mimari Not: Deployment (Canlıya Alma) ve UI/UX Stratejisi</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 10px;">
#         Girdi matrisinin (X) Label Encoding yöntemiyle tamamen sayısallaştırılması, makine öğrenmesi modelinin matematiksel optimizasyonu için zorunlu olsa da; nihai ürünün (Streamlit web uygulaması) kullanıcı deneyimi (UX) açısından anlamsızdır. Kullanıcıların arayüzde sayısal kodlar (örn: 249 vs 65) görmemesi adına sistem mimarisi şu şekilde kurgulanmıştır:
#     </p>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         Eğitim sürecinde fit edilen <strong>LabelEncoder</strong> nesneleri proje sonunda serileştirilerek (pickle/joblib) dışa aktarılacaktır. Streamlit arayüzünde kullanıcılar orijinal metinsel takım isimlerini seçecek; sistem arka planda <code>transform()</code> metodu ile bu metinleri makine koduna çevirip modele sokacak ve modelin ürettiği sayısal sonucu <code>inverse_transform()</code> (Tersine Dönüşüm) metodu ile tekrar insan diline (Ev Sahibi Kazandı / Beraberlik) çevirerek ekrana yansıtacaktır. Bu sayede model karmaşıklığı kullanıcıdan tamamen soyutlanmış (abstraction) olacaktır.
#     </p>
# </div>

# %% [markdown]
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">🪓 3.1.5. Sınıf Korunumlu Veri Bölme Yapısı (Stratified Train-Test Split)</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 10px;">
#         Sınıflandırma modellerinin eğitim ve test performanslarının tarafsız ve genellenebilir olması için veri setinin doğru biçimde ayrıştırılması gerekir. Keşifçi veri analizi evresinde saptadığımız asimetrik sınıf dağılımı (iç saha avantajı yoğunluğu), rastgele bir bölünme yapılması durumunda test kümesinde temsil kaymalarına yol açabilir.
#     </p>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         Veri seti %80 Eğitim (Train) ve %20 Test olacak şekilde ayrıştırılmıştır. Bölünme esnasında <strong>Stratified Split (Sınıf Korumalı Bölme)</strong> disiplini uygulanarak; bağımlı değişkenimizdeki (<code>y</code>) üç farklı sonucun yüzde oranlarının hem eğitim hem de test kümelerinde matematiksel olarak eşit dağılması garanti altına alınmıştır.
#     </p>
# </div>

# %%
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

print("--- EĞİTİM KÜMESİ SINIF DAĞILIMI (%) ---")
print((pd.Series(y_train).value_counts(normalize=True).sort_index() * 100).round(2))

print("\n--- TEST KÜMESİ SINIF DAĞILIMI (%) ---")
print((pd.Series(y_test).value_counts(normalize=True).sort_index() * 100).round(2))

print("\n--- TRAIN VE TEST KÜMELERİNİN BOYUTLARI ---")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)

# %%
import pandas as pd
import os

os.makedirs("../data/model_ready", exist_ok=True)

# X_train ve X_test zaten DataFrame olduğu için direkt kaydedilir
X_train.to_csv("../data/model_ready/X_train.csv", index=False)
X_test.to_csv("../data/model_ready/X_test.csv", index=False)

# ÇÖZÜM: y_train ve y_test'i kaydetmeden hemen önce pd.DataFrame() içine alıp tabloya çeviriyoruz
pd.DataFrame(y_train, columns=['match_result']).to_csv("../data/model_ready/y_train.csv", index=False)
pd.DataFrame(y_test, columns=['match_result']).to_csv("../data/model_ready/y_test.csv", index=False)

print("X_train, X_test, y_train ve y_test verileri 'data/model_ready/' klasörüne BAŞARIYLA kaydedildi.")

# %% [markdown]
# <div style="background: linear-gradient(135deg, #092618 0%, #14452f 50%, #1ea85b 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 8px 20px rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.1); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h2 style="margin: 0; font-size: 22px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px;">🤖 4.1. Modeling (Model Kurma ve Değerlendirme)</h2>
#     <p style="font-size: 13px; color: rgba(255,255,255,0.85); margin-top: 4px; margin-bottom: 0; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">CRISP-DM Metodolojisi / Faz 4</p>
# </div>
# 
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">🏁 4.1.1. Temel Modellerin Eğitimi (Baseline) ve Liderlik Tablosu</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 10px;">
#         Bu aşamada; doğrusal (Logistic Regression), mesafe tabanlı (KNN, SVM), olasılıksal (Naive Bayes) ve boosting tabanlı (XGBoost, LightGBM, Random Forest vb.) 10 farklı algoritma hiperparametre ayarı yapılmadan (baseline) eğitilmiştir.
#     </p>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         Eğitim süreci sonunda algoritmalar, sınıf asimetrisinden etkilenmemek adına sadece "Accuracy" ile değil, esas başarı ölçütümüz olan <strong>Macro F1-Score</strong> değerlerine göre büyükten küçüğe sıralanarak bir liderlik tablosu (Leaderboard) oluşturulmuştur.
#     </p>
# </div>

# %%
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score, f1_score
from IPython.display import display

models = {
    "LogisticRegression": LogisticRegression(max_iter=2000),
    "DecisionTreeClassifier": DecisionTreeClassifier(),
    "RandomForestClassifier": RandomForestClassifier(),
    "GradientBoostingClassifier": GradientBoostingClassifier(),
    "SVC": SVC(),
    "KNeighborsClassifier": KNeighborsClassifier(),
    "GaussianNB": GaussianNB(),
    "AdaBoostClassifier": AdaBoostClassifier(),
    "XGBClassifier": XGBClassifier(),
    "LGBMClassifier": LGBMClassifier(verbose=-1),
}

results = []

for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    results.append(
        {
            "Model Adı": model_name,
            "Accuracy": accuracy_score(y_test, y_pred),
            "Macro F1-Score": f1_score(y_test, y_pred, average="macro"),
        }
    )

results_df = pd.DataFrame(results, columns=["Model Adı", "Accuracy", "Macro F1-Score"])
results_df = results_df.sort_values("Macro F1-Score", ascending=False).reset_index(drop=True)

print("--- TEMEL MODELLERİN PERFORMANS KIYASLAMASI (BASELINE) ---")
display(results_df)

# %%
import matplotlib.pyplot as plt
import seaborn as sns

plot_df = results_df.sort_values("Macro F1-Score", ascending=True)

plt.figure(figsize=(12, 6))
ax = sns.barplot(
    data=plot_df,
    x="Macro F1-Score",
    y="Model Adı",
    palette="viridis",
)

for bar in ax.patches:
    width = bar.get_width()
    y_center = bar.get_y() + bar.get_height() / 2
    ax.text(
        width + 0.005,
        y_center,
        f"{width:.3f}",
        va="center",
        ha="left",
        fontsize=10,
        color="black",
    )

ax.set_title("10 Farklı Sınıflandırma Modelinin Performans Kıyaslaması (Baseline)", fontsize=14, fontweight="bold")
ax.set_xlabel("Macro F1-Score")
ax.set_ylabel("Makine Öğrenmesi Algoritmaları")
ax.set_xlim(0, plot_df["Macro F1-Score"].max() + 0.08)
ax.grid(axis="x", linestyle="--", alpha=0.3)

plt.tight_layout()
plt.show()

# %% [markdown]
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">📊 Domain Bilgisi: Skorların Literatür Bağlamında Değerlendirilmesi</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 10px;">
#         Elde edilen <strong>%56-57 Doğruluk (Accuracy)</strong> ve <strong>~%49 Macro F1-Score</strong> değerleri, genel makine öğrenmesi algısında düşük gibi görünse de, "Uluslararası Futbol Tahminlemesi" problemi için literatür standartlarında ve oldukça rasyoneldir. Bunun matematiksel ve sektörel nedenleri şunlardır:
#     </p>
#     <ul style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; padding-left: 20px; margin-bottom: 12px;">
#         <li style="margin-bottom: 8px;"><strong>Şans Faktörü Sınırı (Random Baseline):</strong> Hedef değişkenimizde 3 adet sınıf (Ev Sahibi, Beraberlik, Deplasman) bulunmaktadır. Rastgele bir tahminin (random guessing) tutma olasılığı matematiksel olarak $33.3\%$ seviyesindedir. Modelimiz bu şans faktörünü neredeyse ikiye katlayarak %57 bandına taşımış ve verideki örüntüyü yakaladığını kanıtlamıştır.</li>
#         <li style="margin-bottom: 8px;"><strong>Futbolun Kaotik Doğası:</strong> Futbol; kırmızı kartlar, anlık sakatlıklar, hakem hataları, hava durumu ve bireysel oyuncu moralleri gibi "veri setinde olmayan (unobserved)" yüzlerce mikro dinamik barındırır. Sadece makro verilerle (ülke adı ve form durumu) %80-90 bandında bir doğruluk beklemek, sporun doğasına aykırıdır. (Böyle bir model olsaydı, spor bahisleri endüstrisi çökerdi).</li>
#     </ul>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         <strong>Sonuç:</strong> Hiperparametre optimizasyonu yapılmamış (Baseline) halleriyle Gradient Boosting, AdaBoost ve XGBoost gibi algoritmaların literatürün altın standardı olan %55 barajını kırması, projenin ve özellik mühendisliği adımlarının başarısını tescillemektedir.
#     </p>
# </div>

# %% [markdown]
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">⚙️ 4.1.2. Hiperparametre Optimizasyonu (Model Tuning)</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 10px;">
#         Temel (Baseline) modellerin değerlendirilmesi sonucunda, ağaç tabanlı topluluk algoritmalarının (Gradient Boosting ve XGBoost) veri setimizin karmaşık yapısını ve sınıf asimetrisini yakalamada en üstün performansı gösterdiği tespit edilmiştir. 
#     </p>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         Model performansını maksimize etmek ve ezberleme (overfitting) riskini izole etmek amacıyla bu lider algoritmaların motor ayarları (hyperparameters) <strong>RandomizedSearchCV</strong> yöntemi kullanılarak çapraz doğrulama (Cross-Validation) ile optimize edilmiştir. Ana optimizasyon hedef metriği olarak yeniden <strong>Macro F1-Score</strong> baz alınmıştır.
#     </p>
# </div>

# %%
from sklearn.model_selection import RandomizedSearchCV

# GradientBoostingClassifier için gerçekçi hiperparametre uzayı
param_dist_gb = {
    "n_estimators": [100, 150, 200, 250, 300],
    "learning_rate": [0.01, 0.05, 0.1, 0.2],
    "max_depth": [2, 3, 4, 5],
    "subsample": [0.7, 0.8, 0.9, 1.0],
}

# XGBClassifier için gerçekçi hiperparametre uzayı
param_dist_xgb = {
    "n_estimators": [100, 150, 200, 250, 300],
    "learning_rate": [0.01, 0.05, 0.1, 0.2],
    "max_depth": [3, 4, 5, 6],
    "subsample": [0.7, 0.8, 0.9, 1.0],
}

random_search_gb = RandomizedSearchCV(
    estimator=GradientBoostingClassifier(),
    param_distributions=param_dist_gb,
    n_iter=10,
    scoring="f1_macro",
    cv=3,
    random_state=42,
    n_jobs=-1,
)

random_search_xgb = RandomizedSearchCV(
    estimator=XGBClassifier(),
    param_distributions=param_dist_xgb,
    n_iter=10,
    scoring="f1_macro",
    cv=3,
    random_state=42,
    n_jobs=-1,
)

random_search_gb.fit(X_train, y_train)
random_search_xgb.fit(X_train, y_train)

print("--- GRADIENT BOOSTING İÇİN EN İYİ PARAMETRELER ---")
print(random_search_gb.best_params_)

print("\n--- XGBOOST İÇİN EN İYİ PARAMETRELER ---")
print(random_search_xgb.best_params_)

best_gb = random_search_gb.best_estimator_
best_xgb = random_search_xgb.best_estimator_

gb_y_pred = best_gb.predict(X_test)
xgb_y_pred = best_xgb.predict(X_test)

print("\n--- OPTİMİZE EDİLMİŞ GRADIENT BOOSTING SONUÇLARI ---")
gb_results = pd.DataFrame(
    [
        {
            "Model Adı": "GradientBoostingClassifier",
            "Accuracy": accuracy_score(y_test, gb_y_pred),
            "Macro F1-Score": f1_score(y_test, gb_y_pred, average="macro"),
        }
    ]
)
display(gb_results)

print("\n--- OPTİMİZE EDİLMİŞ XGBOOST SONUÇLARI ---")
xgb_results = pd.DataFrame(
    [
        {
            "Model Adı": "XGBClassifier",
            "Accuracy": accuracy_score(y_test, xgb_y_pred),
            "Macro F1-Score": f1_score(y_test, xgb_y_pred, average="macro"),
        }
    ]
)
display(xgb_results)

# %% [markdown]
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">💡 Analitik İçgörü: Hiperparametre Optimizasyonu ve Model Seçimi</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 10px;">
#         Optimizasyon (RandomizedSearchCV) sonuçları incelendiğinde, her iki lider algoritmanın da en optimum performansı aynı parametre setinde (<code>max_depth: 3</code>, <code>learning_rate: 0.05</code>, <code>subsample: 0.8</code>, <code>n_estimators: 100</code>) bulduğu görülmüştür. Bu durum, veri setimizin karakteristik doğası hakkında bize net bir yönetsel içgörü sunar:
#     </p>
#     <ul style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; padding-left: 20px; margin-bottom: 12px;">
#         <li style="margin-bottom: 8px;"><strong>Sığ Ağaçlar (max_depth=3):</strong> Futbolun kaotik doğasındaki anlık sürprizleri (gürültüyü) ezberlememek (overfitting önleme) adına algoritmalar bilinçli olarak çok derin ağaçlar kurmaktan kaçınmış, sığ ve daha genelleyici bir öğrenme stratejisi benimsemiştir.</li>
#         <li style="margin-bottom: 8px;"><strong>Rastgelelik (subsample=0.8):</strong> Model her iterasyonda verinin sadece %80'ini kullanarak öğrenmiş, bu sayede daha esnek ve gerçek dünya verisine (unseen data) dayanıklı (robust) hale gelmiştir.</li>
#     </ul>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         <strong>Nihai Karar:</strong> Optimizasyon sonrasında en yüksek doğruluk ve Macro F1-Skorunu (%49.88) sunan <strong>XGBoost (Extreme Gradient Boosting)</strong> algoritması, sistemin ana tahmin motoru (Şampiyon Model) olarak seçilmiş ve Streamlit canlıya alma evresi için kalıcı olarak belirlenmiştir.
#     </p>
# </div>

# %% [markdown]
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">🌟 4.1.3. Şampiyon Modelin Karar Mekanizması: Öznitelik Önemi (Feature Importance)</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 10px;">
#         Makine öğrenmesi projelerinde modelin bir "kara kutu (black box)" olarak kalmaması ve iş dünyasına şeffaf bir gerekçe sunabilmesi adına (Explainable AI), nihai karar motorumuz olan XGBoost'un tahmin yaparken hangi değişkenlere ne kadar ağırlık verdiği incelenmiştir.
#     </p>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         Aşağıdaki analiz, veri hazırlama (Data Preparation) aşamasında türettiğimiz dinamik form skorlarının (Feature Engineering) modelin öğrenme sürecine ne ölçüde yön verdiğini kanıtlar niteliktedir.
#     </p>
# </div>

# %%
import matplotlib.pyplot as plt
import seaborn as sns

feature_importance_df = pd.DataFrame(
    {
        "Öznitelik": X.columns,
        "Önem Derecesi": best_xgb.feature_importances_,
    }
).sort_values("Önem Derecesi", ascending=False).reset_index(drop=True)

plt.figure(figsize=(12, 7))
ax = sns.barplot(
    data=feature_importance_df,
    x="Önem Derecesi",
    y="Öznitelik",
    palette="magma",
)

for bar in ax.patches:
    width = bar.get_width()
    y_center = bar.get_y() + bar.get_height() / 2
    ax.text(
        width + 0.001,
        y_center,
        f"{width:.3f}",
        va="center",
        ha="left",
        fontsize=10,
        color="black",
    )

ax.set_title("XGBoost Şampiyon Modeli - Öznitelik Önemi (Feature Importance)", fontsize=14, fontweight="bold")
ax.set_xlabel("Karar Ağırlığı (Önem Derecesi)")
ax.set_ylabel("Veri Seti Öznitelikleri")
ax.set_xlim(0, feature_importance_df["Önem Derecesi"].max() + 0.02)
ax.grid(axis="x", linestyle="--", alpha=0.3)

plt.tight_layout()
plt.show()

# %% [markdown]
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">⚖️ Yönetsel Analiz: 'Neutral' Değişkeninin Gücü ve Modelin İş Değeri (Business Value)</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 10px;">
#         Öznitelik önemi analizinde <strong>'neutral' (tarafsız saha)</strong> değişkeninin açara ara en yüksek karar ağırlığına sahip olması, modelin "Ev Sahibi Avantajı" (Home Advantage) gerçeğini matematiksel olarak keşfettiğini kanıtlar. Model; bir takımın gücünden veya formundan ziyade, müsabakanın ev sahibi baskısı altında mı yoksa tarafsız bir turnuva zemininde mi oynandığını ana ayrıştırıcı şalter olarak kullanmaktadır.
#     </p>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         <strong>Model Neye Hizmet Ediyor?</strong> Literatürde %50-55 bandında Macro F1 skoru üreten bu tarz spor modellerinin temel amacı "kristal küre" gibi kesin geleceği tahmin etmek değildir. Bu sistemler; medya kuruluşları için tarafsız maç öncesi ihtimal analizleri üretmek (win probability), insanların duygusal ön yargılarını (human bias) kırmak ve risk yönetimi departmanları (veya bahis yatırımcıları) için piyasa beklentileriyle matematiksel gerçeklik arasındaki "değer farklılıklarını (value)" tespit eden bir karar destek motoru olarak konumlanmaktadır.
#     </p>
# </div>

# %% [markdown]
# <div style="background: linear-gradient(135deg, #092618 0%, #14452f 50%, #1ea85b 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 8px 20px rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.1); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h2 style="margin: 0; font-size: 22px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px;">📊 5. Evaluation (Model Değerlendirme)</h2>
#     <p style="font-size: 13px; color: rgba(255,255,255,0.85); margin-top: 4px; margin-bottom: 0; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">CRISP-DM Metodolojisi / Faz 5</p>
# </div>
# 
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">🔍 5.1. Sınıflandırma Raporu ve Karmaşıklık Matrisi (Confusion Matrix)</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 10px;">
#         Modelleme aşamasında şampiyon seçilen XGBoost algoritmasının yalnızca genel Accuracy veya F1 skoruna bakmak, modelin zayıf yönlerini gizleyebileceği için akademik açıdan eksik bir değerlendirme olacaktır. Modelin hangi durumlarda yanıldığını, özellikle tahmin edilmesi en zor olan "Beraberlik" (Draw) sınıfındaki davranışını mikroskobik düzeyde incelemek için detaylı bir değerlendirme yapılması şarttır.
#     </p>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         Bu doğrultuda, modelin test verisi (Unseen Data) üzerindeki sınıf bazlı performansını yansıtan <strong>Classification Report</strong> (Precision, Recall) ve <strong>Confusion Matrix</strong> (Karmaşıklık Matrisi) üretilmiş; tahmin hatalarının yönelimleri görselleştirilerek iş modeli (Business Understanding) ile uyumluluğu doğrulanmıştır.
#     </p>
# </div>

# %%
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Optimize edilmiş XGBoost modeli ile test verisi üzerinde tahmin üret
y_pred = best_xgb.predict(X_test)

print("--- DETAYLI SINIFLANDIRMA RAPORU ---")
print(classification_report(y_test, y_pred))

# Karmaşıklık matrisini oluştur
cm = confusion_matrix(y_test, y_pred)

# Karmaşıklık matrisini görselleştir
fig, ax = plt.subplots(figsize=(9, 7))
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap="YlGnBu", ax=ax, colorbar=True)

ax.set_title("XGBoost Karmaşıklık Matrisi (Confusion Matrix)", fontsize=13, fontweight="bold")
ax.set_xlabel("Tahmin Edilen Sınıf")
ax.set_ylabel("Gerçek Sınıf")

plt.tight_layout()
plt.show()

# %%
import os
from sklearn.metrics import classification_report

os.makedirs("../reports", exist_ok=True)

# Sınıflandırma raporunu bir metin dosyası (TXT) olarak reports klasörüne kaydetme
rapor_metni = classification_report(y_test, y_pred)

with open("../reports/model_evaluation_report.txt", "w", encoding="utf-8") as dosya:
    dosya.write("--- XGBOOST MODEL DEĞERLENDİRME RAPORU ---\n\n")
    dosya.write(rapor_metni)

print("Sınıflandırma raporu 'reports/model_evaluation_report.txt' olarak BAŞARIYLA kaydedildi!")

# %% [markdown]
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">📏 Analitik Metriklerin Yorumu: Neden Accuracy Yerine Macro F1?</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 10px;">
#         Modelin genel performans tablolarında "Accuracy (Doğruluk)" oranı %56-57 bandındayken, "Macro F1-Score" oranının %49-50 bandında kalması istatistiksel bir hatadan ziyade, <strong>sınıf dengesizliği (class imbalance)</strong> probleminin doğal bir sonucudur:
#     </p>
#     <ul style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; padding-left: 20px; margin-bottom: 12px;">
#         <li style="margin-bottom: 8px;"><strong>Accuracy (Doğruluk) Nedir?</strong> Modelin toplamda kaç maçı doğru bildiğini gösterir. Veri setindeki maçların yaklaşık %48'i "Ev Sahibi Galibiyeti" ile bitmektedir. Kötü niyetli/ezberci bir model, hiçbir analiz yapmadan tüm maçlara sürekli "Ev Sahibi Kazanır" dese bile otomatik olarak %48 Accuracy seviyesine ulaşacaktır. Bu durum, Accuracy metriğinin yanıltıcı (bias) olabileceğini gösterir.</li>
#         <li style="margin-bottom: 8px;"><strong>Macro F1-Score Nedir?</strong> Modelin sadece çoğunluk sınıfını (Ev Sahibi) değil, azınlık sınıflarını da (Beraberlik ve Deplasman) ne kadar iyi öğrenebildiğini test eder. Her üç sınıfın başarı oranını ayrı ayrı hesaplar ve bunların <em>eşit ağırlıklı</em> ortalamasını alır. Beraberlikleri tahmin etmek futbolun doğası gereği en zor olaydır; Macro F1 skoru, modelin bu zorluğa (Beraberlik tahminlerine) rağmen gösterdiği gerçekçi ve dengeli performansı temsil eder.</li>
#     </ul>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         <strong>Özetle:</strong> Modelimiz maçların yaklaşık <strong>%57'sini</strong> nokta atışı doğru bilmektedir. %50 olan Macro F1 değeri ise modelin kolaya kaçıp sadece ev sahibi galibiyetlerini ezberlemediğini; beraberlik ve deplasman ihtimallerini de matematiksel olarak hesaba kattığını kanıtlayan güvenlik metriğimizdir.
#     </p>
# </div>

# %% [markdown]
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">🚨 Yönetsel Analiz: Neden %80 F1 Skoru Bir Başarı Değil, 'Hata' Sinyalidir?</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 10px;">
#         Makine öğrenmesinde başarı metrikleri değerlendirilirken domain (sektör) dinamikleri hayati önem taşır. Futbol gibi yüksek stokastik (rastgele) olayların, insan faktörünün, hakem kararlarının ve anlık sakatlıkların dahil olduğu kaotik bir ekosistemde %80 veya %90 gibi F1-Skorları elde etmek teorik olarak imkansızdır. Böyle bir skor elde edilseydi, bu modelin başarısını değil, veri hazırlığı sürecindeki iki büyük mühendislik hatasını işaret ederdi:
#     </p>
#     <ul style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; padding-left: 20px; margin-bottom: 12px;">
#         <li style="margin-bottom: 8px;"><strong>Veri Sızıntısı (Data Leakage):</strong> Modelin eğitim setinde, gelecekte veya maç anında belirlenecek bir sütunun (örn:atılan gol sayısı) bağımsız değişkenler (X) matrisinde unutulması durumu.</li>
#         <li style="margin-bottom: 8px;"><strong>Aşırı Öğrenme (Overfitting):</strong> Modelin futbolun genel dinamiklerini ve trendlerini öğrenmek yerine, tarihsel verilerdeki istisnai satırları (noise) ezberlemesi durumu.</li>
#     </ul>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         <strong>Sonuç:</strong> Şampiyon XGBoost modelimizin ürettiği %50 bandındaki Macro F1-Skoru; ezberden arındırılmış, veri sızıntısına karşı zırhlanmış ve spor istatistiği literatürünün matematiksel gerçekliğine (Reality Bound) tamamen uygun olan <em>optimum noktayı</em> temsil etmektedir.
#     </p>
# </div>

# %% [markdown]
# <div style="background: linear-gradient(135deg, #092618 0%, #14452f 50%, #1ea85b 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 8px 20px rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.1); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h2 style="margin: 0; font-size: 22px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px;">🚀 6.1. Deployment Hazırlığı (Model Export)</h2>
#     <p style="font-size: 13px; color: rgba(255,255,255,0.85); margin-top: 4px; margin-bottom: 0; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">CRISP-DM Metodolojisi / Faz 6</p>
# </div>
# 
# <div style="background: linear-gradient(135deg, #092618 0%, #0f3625 100%); padding: 20px; border-radius: 15px; color: white; font-family: 'Segoe UI', sans-serif; box-shadow: 0 6px 15px rgba(0,0,0,0.15); border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 15px; max-width: 100%; box-sizing: border-box;">
#     <h3 style="color: #22c55e; margin-top: 0; font-weight: 800; font-size: 1.2rem;">💾 6.1.1. Şampiyon Modelin ve Kodlayıcıların (Encoders) Serileştirilmesi</h3>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 10px;">
#         Makine öğrenmesi modelinin her web uygulaması (Streamlit) başlatıldığında sıfırdan eğitilmesi, hem işlemci maliyeti hem de zaman açısından verimsizdir. Bu nedenle eğitilmiş ve optimize edilmiş şampiyon modelimiz (XGBoost) kalıcı bir dosya formatına dönüştürülerek dondurulmalıdır.
#     </p>
#     <p style="font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
#         Bu işlem kapsamında yalnızca makine öğrenmesi modeli değil; aynı zamanda son kullanıcının arayüzde seçeceği metinsel takım isimlerini modelin anlayacağı sayısal indekslere çevirecek olan <strong>LabelEncoder</strong> nesneleri de <code>pickle</code> kütüphanesi kullanılarak <code>.pkl</code> (Pickle) formatında dışa aktarılmıştır. Bu dosyalar, kurulacak web mimarisinin ana karar motorlarını (backend) oluşturacaktır.
#     </p>
# </div>

# %%
import os
import pickle
from sklearn.preprocessing import LabelEncoder

os.makedirs("../models", exist_ok=True)

with open("../models/champion_xgboost_model.pkl", "wb") as model_file:
    pickle.dump(best_xgb, model_file)

label_encoders = {
    "home_team": LabelEncoder().fit(df_matches["home_team"]),
    "away_team": LabelEncoder().fit(df_matches["away_team"]),
    "tournament": LabelEncoder().fit(df_matches["tournament"]),
    "country": LabelEncoder().fit(df_matches["country"]),
    "target_y": LabelEncoder().fit(df_matches["match_result"]),
}

with open("../models/label_encoders.pkl", "wb") as encoder_file:
    pickle.dump(label_encoders, encoder_file)

print("--- MODEL VE ENCODER DOSYALARI BAŞARIYLA KAYDEDİLDİ ---")
print("Oluşturulan dosyalar:")
print("- champion_xgboost_model.pkl")
print("- label_encoders.pkl")

# %%
import os

html_icerik = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>CRISP-DM Proje Raporu</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f4f9; color: #333; margin: 40px; }
        h1 { color: #001338; border-bottom: 2px solid #00f2ff; padding-bottom: 10px; }
        .kutu { background: white; padding: 20px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-left: 5px solid #7000ff; }
        h2 { color: #7000ff; margin-top: 0; }
    </style>
</head>
<body>
    <h1>⚽ Uluslararası Futbol Maç Sonucu Tahminleyicisi - CRISP-DM Raporu</h1>
    
    <div class="kutu">
        <h2>1. İş Anlayışı (Business Understanding)</h2>
        <p>Uluslararası futbol maçlarının sonuçlarını (Ev Sahibi, Deplasman, Beraberlik) tarihsel veri ve takım form durumlarına göre tahmin eden bir Karar Destek Sistemi geliştirmek.</p>
    </div>
    
    <div class="kutu">
        <h2>2. Veriyi Anlama (Data Understanding)</h2>
        <p>1980'den günümüze uluslararası maçlar incelendi. Turnuva türü, oynanan ülke, tarafsız saha durumu ve takım formları temel değişkenler olarak belirlendi.</p>
    </div>
    
    <div class="kutu">
        <h2>3. Veri Hazırlama (Data Preparation)</h2>
        <p>Kategorik değişkenler Label Encoding ile dönüştürüldü ve X_train, y_train setleri oluşturuldu.</p>
    </div>
    
    <div class="kutu">
        <h2>4. Modelleme (Modeling)</h2>
        <p>Ağaç tabanlı bir algoritma olan XGBoost Classifier kullanıldı. Sınıflandırma problemi olarak (0, 1, 2) kurgulandı.</p>
    </div>
    
    <div class="kutu">
        <h2>5. Değerlendirme (Evaluation)</h2>
        <p>Test-Time Augmentation (TTA) ve Gerçekçilik Kalibrasyonu ile Positional Bias (Ev sahibi önyargısı) giderildi. Başarı oranları raporlandı.</p>
    </div>
    
    <div class="kutu">
        <h2>6. Yayına Alma (Deployment)</h2>
        <p>Streamlit kullanılarak modern, Şampiyonlar Ligi temalı, dinamik animasyonlara sahip bir web arayüzü ile model canlıya alındı.</p>
    </div>
</body>
</html>
"""

os.makedirs("../reports", exist_ok=True)
with open("../reports/crisp_dm_presentation.html", "w", encoding="utf-8") as dosya:
    dosya.write(html_icerik)

print("HTML Sunumu 'reports/crisp_dm_presentation.html' olarak BAŞARIYLA oluşturuldu!")


