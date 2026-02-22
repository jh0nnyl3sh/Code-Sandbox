import os # -> işletim sistemiyle çalışacağız.

#klasörümüzün adı
folder_name = "TEST_ALANI"

# 1. Eğer klasör yoksa oluştur.
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"📁 '{folder_name}' klasörü oluşturuldu.")
    

# 2. İçine sahte dosyalar yaratalım.
files_to_create = [
    "rapor_2026.txt", "tatil.jpg", "butce.xls",
    "dava_dosyasi.pdf", "resim1.jpg", "notlar.txt",
    "sifreler.txt", "sunum.pptx", "virus.exe"
]

# Dosyaların içine boş veri basıp kaydediyoruz. 
for file in files_to_create:
    # os.path.join -> Windows/Mac uyumlu yol yapar (TEST_ALANI/dosya.txt)
    full_path = os.path.join(folder_name, file)
    
    with open(full_path, "w") as f:
        f.write("Bu bir test dosyasidir.")
        
    print(f"➕ Oluşturuldu: {file}")
    
print("\n✅ ORTALIK KARIŞTIRILDI! Şimdi 'organizer.py' ile temizle.")
    
    