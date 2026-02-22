import time

# Kendi yazdığımız dosyayı import edelim.
import my_arsenal as arsenal

print("🤠 SALDIRI SENARYOSU BAŞLATILIYOR...")
print("-" * 30)

target_pass = input("Hedef sistemin şifresini gir (Simülasyon): ")

# 1 önce şifre güçlü mü diye analiz et
if arsenal.check_password_strength(target_pass):
    print(f"Analiz : '{target_pass}' güçlü bir şifre. Brute-Force zor olabilir.")

else:
    print(f"Analiz : '{target_pass}' çok zayıf! Hemen kırılabilir.")
    
time.sleep(1) # -> 1 saniye bekletiyoruz


# 2 brute force dene
print("\nBrute-Force Aracı Çalıştırılıyor...")
result = arsenal.brute_force_simulator(target_pass)

if result == True:
    print("💥 BAŞARILI : Şifre wordlist içinde bulundu ve sistem hacklendi.")
    
else:
    print("🛡️ BAŞARISIZ. Şifre listede yok, sistem güvenli.")

