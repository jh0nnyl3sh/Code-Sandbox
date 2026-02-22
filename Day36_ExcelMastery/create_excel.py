import pandas as pd

print("[CERBERUS ANALİSTİ] Devreye Girdi...\n")

# 1. VERİ SETİ OLUŞTURMA (Dünkü sözlük yapısınınaynısı!)
# Gerçek hayatta bu verileri veritabanından veya başka bir dosyadan çekeceğiz.

adliye_verisi = {
    "Dosya_No" : ["2026/101", "2026/102", "2026/103", "2026/104"],
    "Taraf_Bilgisi" : ["Ahmet Y. - Ayşe T. - ", "Mehmet K. - Şirket A.Ş.",
                       "Hasan B. - Veli C.", "Zeynep D. - SGK" ],
    "Dava_Turu" : ["Boşanma", "Alacak", "Ceza", "İşe İade"],
    "Durum" : ["Açık", "Karara Çıktı", "Açık", "İstinafta"],
    "Masraf_TL" : [1500, 4300, 0, 2100]
}


# 2. DATAFRAME OLUŞTURMA (Veriyi Tabloya Çevirme)
# DataFrame (df), Pandas'ın Excel tablosuna verdiği isimdir. Satırlar ve sütunlardan oluştur.

print("⚙️ Veriler Pandas DataFrame (Tablo) formatına dönüştürülüyor...")
df = pd.DataFrame(adliye_verisi)

# Tablonun terminalde nasıl göründüğüne bir bak : 
print("\n📊 SANAL TABLO GÖRÜNÜMÜ: ")
print(df)
print("-" * 50)


# 3. FİZİKSEL EXCEL DOSYASINA ÇEVİRME (The Magic)
dosya_adi = "Sanal_Tevzi_Raporu.xlsx"

# index=False diyoruz çünkü Pandas'ın kendi koyduğu 0,1,2,3 sıra numaralarını Excel'de görmek istemiyoruz.
df.to_excel(dosya_adi, index=False)

print(f"\n✅ İŞLEM TAMAM! Dosya üretildi: '{dosya_adi}'")