"""
MY ARSENAL (Kişisel Hacking Kütüphanesi)
Bu dosya tek başına çalıştırılmaz, import edilir.
"""

def check_password_strength(password):
    forbidden = ["admin", "1234", "password"]
    
    if len(password) < 8:
        return False
    
    for bad_word in forbidden:
        if bad_word in password:
            return False
        
    return True



def brute_force_simulator(target):
    # Simüle edilmiş bir brute force (True dönerse kırıldı demektir.)
    # Basit olsun diye sadece lsitede var mı bakıyoruz.

    wordlist = ["123456", "admin", "root", "user", "hunter2026"]
    
    if target in wordlist:
        return True
    else:
        return False
    
    
    # --- KORUMA KALKANI ---
    # Bu blok, dosya import edildiğinde ÇALIŞMAZ.
    # Sadece bu dosyayı direkt test ederken çalışır.
    
    if __name__ == "__main__":
        print("Kütüphane Test Modu Çalışıyor...")
        print(check_password_strength("admin123")) # False bekliyoruz.