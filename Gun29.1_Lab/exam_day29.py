def is_password_strong(password):
    if "admin" in password or "1234" in password:
        print("❌ Hata: Şifre yasaklı kelimelerden oluşuyor.")
        return False
    
    elif len(password) < 8:
        print("❌ Hata: Şifre en az 8 karakter olamalı.")
        return False
    
    else:
        return True
    
    
    
# --- ANA PROGRAM ---
user_input = input("Şifre giriniz : ").strip().lower()

sonuc = is_password_strong(user_input)

if sonuc == True:
    print("✅ Şifre güvenli ve onaylandı")

else:
    print("⚠️ Lütfen başka bir şifre deneyin")