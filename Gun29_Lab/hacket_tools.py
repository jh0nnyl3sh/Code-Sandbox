import time

# --- TOOLBOX (ARAÇ ÇANTASI) ---

# Yaş kontrolü fonksiyonu

def check_age(age):
    """
    Dışarıdan gelen 'age' (int) bilgisini kontrol eder.
    İçeride input yoktur.
    """
    
    if str(age).isdigit():
        age = int(age)
        
        if 18 <= age <= 120:
            print(f"✅ Yaş {age} : Giriş Onaylandı.")
        
        else:
            print(f"✋🏼 Yaş {age} : Erişim Reddedildi.")
    
    else:
        print("⚠️Hata : Yaş bilgisi sayısal olmalıdır.")
        

# brute force kontrolü

def brute_force(target_password):
    """
    Dışarıdan verilen 'target_password'ü, kendi içindeki wordlistte arar.
    """
    
    
    # Saldırganın elindeki liste (Veritabanı)
    wordlist = ["admin", "123456", "password", "hunter2026",
                "root", "patron", "admin123321"]
    
    print(f"\nHEDEF : '{target_password}' için saldırı başlatırılıyor...")
    print("-" * 40)

    deneme_sayaci = 0
    found = False # -> bulundu mu bayrağı
    
    for guess in wordlist:
        deneme_sayaci += 1
        time.sleep(1)
        
        if guess == target_password:
            print(f"💥 BİNGO! Şifre Kırıldı : '{guess}'")
            print(f"İstatistik : {deneme_sayaci}. denemede bulundu")
            found = True
            break
        
        else:
            print(f"❌ Deneme {deneme_sayaci}: '{guess} -> Başarısız'")
            
    if not found:
        print("\nSonuç : Şifre bu listede yok.")
        
        
# ---- ANA KOMUTA MERKEZİ (TEST ALANI) ----

# 1. yaş kontrolünü test edelim.
check_age(25)
check_age(12)

# 2. brute force test et
# senerayo : hedef şifre 'hunter2026'. bakalım listede bulabilecek mi?

brute_force('hunter2026')

# seneryo 2 : listede olmayan bir şifre
brute_force('cok_zor_sifre_')