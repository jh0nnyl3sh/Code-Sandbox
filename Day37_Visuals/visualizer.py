import pandas as pd # -> Excel ile top gibi oynar
import matplotlib.pyplot as plt # -> Veri görselleştirmek için şart

print("🐺 [CERBERUS GÖRSEL İSTİHBARAT] Başlatıldı...\n")

# 1. VERİ SETİ -> Neyin üzerinde çalışacağız ?
# Bunu pd.read_excel() ile okuruz ancak işin mantığını görmek için
# şuan elle yazalım. neyi neden yaptığımı, arkada çalışan mantığı kavrayalım.

tevzi_verisi = {
    "Dava_Turu": ["Boşanma", "İş Mahkemesi", "Ceza", "Tüketici", "İcra"],
    "Dosya_Sayisi": [450, 320, 600, 150, 850]
}

# Veriyi Pandas Tablosuna (DataFrame) çeviriyoruz.
df = pd.DataFrame(tevzi_verisi)
print("⚙️ Veriler toblaya dönüştürüldü. Grafiğe dökülüyor...")


# 2. GRAFİK İNŞASI (Matplotlib Büyüsü)
# plt.figure() ile grafiğin boyutunu (genişlik, yükseklik) inç cinsinden belirliyoruz.

plt.figure(figsize=(10, 6)) # 10 inc genişlik 6 inc yükseklik

# Çubuk grafiği (Bar Chart) oluşturalım.
# x eksenine Dava Türü, y eksenine Dosya Sayısı gelecek.
plt.bar(df["Dava_Turu"], df["Dosya_Sayisi"], color="#2c3e50") # Hex renk kodu (koyu larcivert)

# 3. MAKYAJ VE DÜZENLEME (Grafiği kurumsal hale getirme)
plt.title("2026 Yılı - Mahkemelere Göre Dağıtılan Dosya Sayıları", fontsize=14, fontweight="bold")
plt.xlabel("Mahkeme / Dava Türü", fontsize=12)
plt.ylabel("Toplam Dosya Sayısı", fontsize=12)

# Arka plana hafif bir ızgara (grid) ekleyelim ki sayılar daha rahat okunsu.
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 4. ÇIKTIYI KAYDETME (Asıl olay!)
resim_adi = "Tevzi_Istatistik_Raporu.png"

# plt.show() dersek ekrana pencere açılır
# Ama biz otomasyoncuyuz! Direkt masasütüne / klasöre resim olarak kaydediyoruz
plt.savefig(resim_adi, dpi=300, bbox_inches='tight') # dpi=300 yüksek kalite demektir.

print(f"✅ İŞLEM TAMAM! Kurumsal grafik üretildi : {resim_adi}")