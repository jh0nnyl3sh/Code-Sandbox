import pandas as pd

print("[CERBERUS ANALİSTİ] Dosyalar İnceleniyor...")

# 1. DOSYAYI OKUMAK 
dosya_adi = "Sanal_Tevzi_Raporu.xlsx"
df = pd.read_excel(dosya_adi)

print("📁 Orijinal Dosya Başarıyla Okundu. Toplam Kayıt : ", len(df))

# 2. FİLTRELEME (işte büyü burada başlıyor)
# Excel'de "Filtre -> Durum -> Sadece Açık olanları seç" işleminin koddaki karşılığı
acik_dosyalar_df = df[df["Durum"] == "Açık"]

print("\n 🔍 SADECE 'AÇIK' DURUMDAKİ DOSYALAR: ")
print(acik_dosyalar_df)

# 3. MATEMATİKSEL ANALİZ (Hesap makinesini çöpe at)
# Masraf_TL sütunundaki tüm değerleri topla
toplam_masraf = df["Masraf_TL"].sum()
ortalama_masraf = df["Masraf_TL"].mean()

print("-" * 40)
print("💰 FİNANSAL ÖZET: ")
print(f"Toplam Masraf :  {toplam_masraf}")
print(f"Ortalama Masraf : {ortalama_masraf}")
print("-" * 40)

# 4. YENİ RAPORU KAYDETMEK
# Sadece "Açık" olan dosyaları YENİ bir Excel olarak kaydediyoruz.
# Orijinal dosya bozulmuyor.
yeni_rapor_adi = "Acik_Dosyalar_Raporu.xlsx"
acik_dosyalar_df.to_excel(yeni_rapor_adi, index=False)

print(f"\n✅İSTİHBARAT RAPORU HAZIR : '{yeni_rapor_adi}' dosyasına kaydedildi.")

