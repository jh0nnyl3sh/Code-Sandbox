"""
Bu motorun tek bir görevi var : Veriyi almak, Pandas
ile amelelik yapmadan saniyeler içinde filtrelemek,
Excel'e basmak ve diğer motorların kullanması için 
hazırda tutmak.
"""

import pandas as pd

def process_data():
    print("⚙️ [DATA ENGINE] Veri çekiliyor ve işleniyor...")

    # 1. HAM VERİ (Gerçek. hayatta bu kısım API'den veya başka kaynaktan
    # gelen bir JSON/Excel olur)
    raw_data = {
        "Dosya_No": ["2026/101", "2026/102", "2026/103", "2026/104", "2026/105"],
        "Dava_Turu": ["Boşanma", "Ceza", "İcra", "Ceza", "İş Mahkemesi"],
        "Durum": ["Açık", "Karara Çıktı", "Açık", "Açık", "İstinafta"],
        "Masraf_TL": [1500, 4300, 250, 0, 2100]
    }
    
    # Veriyi Pandas'ın beynine (DataFrame) yüklüyoruz.
    df = pd.DataFrame(raw_data)
    
    # 2. FİLTRELEME (Sadece 'Açık' olan kritik dosyaları ayıkla)
    filtered_df = df[df["Durum"] == "Açık"]
    
    # 3. KANIT OLUŞTURMA (Excel'e bas)
    excel_filename = "Guncel_Acik_Dosyalar.xlsx"
    filtered_df.to_excel(excel_filename, index=False)
    
    print(f"✅ [DATA ENGINE] Veri filtrelendi ve '{excel_filename}' dosyası üretildi.")

    # 4. MİMARİ BAĞLANTI (İşte modüler programlama budur!)
    # Bu verileri havaya uçurmuyoruz, Grafiği çizecek ve -
    # Mail atacak motorlar için "Geri Döndürüyoruz" (Return)
    return filtered_df, excel_filename

if __name__ == "__main__":
    process_data
    
    
