import os
import shutil

target_folder = "TEST_ALANI"
print(f"🕵️‍♂️ HEDEF: {os.path.abspath(target_folder)} taranıyor...\n")

# Eğer klasör yoksa uyar ve çık
if not os.path.exists(target_folder):
    print("❌ HATA: 'TEST_ALANI' klasörü bulunamadı! Önce setup_mess.py çalıştır.")
    exit()

extensions = {
    "Resimler": [".jpg", ".png", ".jpeg"],
    "Belgeler": [".txt", ".pdf", ".xls", ".pptx"],
    "Tehlikeli": [".exe", ".bat"]
}

# 1. Klasörleri Oluştur
for category in extensions.keys():
    folder_path = os.path.join(target_folder, category)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"📁 Klasör Açıldı: {category}")

# 2. Dosyaları Taşı (Hata Yakalamalı)
files_list = os.listdir(target_folder)
print(f"🔍 Bulunan Toplam Öğe Sayısı: {len(files_list)}")

for filename in files_list:
    source_path = os.path.join(target_folder, filename)
    
    # Klasörleri atla
    if os.path.isdir(source_path):
        continue

    moved = False
    for category, exts in extensions.items():
        for ext in exts:
            if filename.lower().endswith(ext):
                # Hedef KLASÖR yolu (Dosya adı değil, klasör yolu)
                dest_folder = os.path.join(target_folder, category)
                
                # Hedefte bu dosya var mı kontrolü
                dest_file_path = os.path.join(dest_folder, filename)
                if os.path.exists(dest_file_path):
                    print(f"⚠️  ATLANDI: '{filename}' zaten {category} içinde var.")
                    moved = True
                    break

                try:
                    # shutil.move(kaynak, HEDEF_KLASÖR) -> Dosyayı klasörün içine atar
                    shutil.move(source_path, dest_folder)
                    print(f"✅ TAŞINDI: {filename} >>> {category}")
                    moved = True
                except Exception as e:
                    print(f"❌ HATA: {filename} taşınamadı! Sebep: {e}")
                
                break # Uzantı bulundu, döngüden çık
        if moved:
            break

print("\n✨ İŞLEM TAMAMLANDI ✨")