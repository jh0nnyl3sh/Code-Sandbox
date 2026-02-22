import time # Bekleme süresini eklemek için

# hedef kasanın şifresi
TARGET_PASSWORD = "hunter2026"

# Deneme lsitesi (wordlist)
wordlist = ["123456", "admin", "password", "jhony123",
            "hunter2026", "root", "111111"]

print("Brute-Force Saldırısı Başlatılıyor...\n")

# sayaç
attempt_count = 0

for guess in wordlist:
    attempt_count += 1 # her göngüde sayacı 1 attırıyoruz
    
    # gerçeklik katmak için her denemede yarım saniye (0.5) bekle
    time.sleep(0.5)
    
    if guess == TARGET_PASSWORD:
        print(f"🚨 BİNGO! Şifre Kırıldı : '{guess}'")
        print(f"İstatistik : Toplam {attempt_count} denemede başarılı oldu")
        print("Saldırı bitti. Kasa açılıyor...")
        break
    else:
        print(f"❌ Deneme {attempt_count} : '{guess}' -> Başarısız")

print("\n--- Operasyon Tamamlandı ---")
