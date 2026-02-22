import matplotlib.pyplot as plt

def create_chart(df):
    print("📊 [VISUAL ENGINE] Veriler görselleştiriliyor...")
    
    # Eğer gelen veri tablosu (df) boşsa, sistemin çökmemesi için güvenlik önlemi
    if df.empty:
        print("⚠️ [VISUAL ENGINE] Çizilecek açık dosya bulunamadı!")
        return None
    
    # 1. GRAFİK İNŞASI
    # Dava Türüne göre 'Açık' dosyaların sayısını gruplayıp sayıyoruz (.value_counts)
    dava_sayilari = df["Dava_Turu"].value_counts()
    
    plt.figure(figsize=(8, 5))
    
    # Çubuk grafiğini çiziyoruz. (Koyu Kırmızı Red Team rengi!)
    dava_sayilari.plot(kind="bar", color="#8b0000")
    
    # 2. MAKYAJ
    plt.title("Güncel Açık Dosyaların Türlere Göre Dağılımı", fontsize=12, fontweight="bold")
    plt.xlabel("Dava Türü", fontsize=10)
    plt.ylabel("Dosya Sayısı", fontsize=10)
    plt.xticks(rotation=0) # Alttaki yazıların düz durması için
    plt.grid(axis='y', linestyle="--", alpha=0.7)
    
    # 3. KANIT OLUŞTURMA (Resmi kaydet)
    chart_filename = 'Acik_Dosyalar_Grafigi.png'
    plt.savefig(chart_filename, dpi=300, bbox_inches='tight')
    plt.close() # RAM'i şişirmemek için arka plandaki çizim tahtasını temizliyoruz.
    
    print(f"✅ [VISUAL ENGINE] Kurumsal grafik üretildi : '{chart_filename}'")
    
    # Şalter (main_operator) bu resmin adını isteyecek ki mail'e ekleyebilsin.
    return chart_filename

# Test bloğu (Sadece bu dosyayı test etmek istersek)

if __name__ == "__main__":
    # Test için Data Engine'i çağırıyoruz (Modüllerin gücü)
    from data_engine import process_data
    
    # Veri motorunu çalıştır, ondan gelen 'df'yi (tabloyu) al
    test_df, test_excel = process_data()
    
    # O tabloyu görsel motora ver
    create_chart(test_df)
    