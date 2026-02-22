"""
Day 27: The Interrogator (Sorgucu)
Kullanıcıdan geçerli bir yaş verisi alana kadar döngüden çıkmayan,
hatalara karşı 'try-except' ile güçlendirilmiş bot.
"""

while True:
    try:
        # 1. Veriyi Al ve Temizle (Boşlukları siler)
        user_input = input("Lütfen yaşınızı giriniz: ").strip()
        
        # 2. Direkt Çevirmeyi Dene (Riskli Hareket!)
        # Eğer kullanıcı harf girerse, kod burada 'ValueError' patlatır 
        # ve aşağıdaki 'except' bloğuna ışınlanır.
        age = int(user_input)

        # 3. Mantık Kontrolü (Business Logic)
        if 18 <= age <= 120:
            print(f"✅ Giriş Onaylandı! Hoş geldin Agent ({age}).")
            break # Döngüyü kır ve özgürlüğe koş
        
        elif age > 120:
            print("🧛‍♂️ Hata: Vampirler giremez! (120'den küçük olmalı)")
            
        else:
            print("⛔ Erişim Reddedildi! Büyü de gel.")

    except ValueError:
        # 4. Hata Yakalama (The Safety Net)
        # int() fonksiyonu başarısız olursa kod buraya düşer.
        print("⚠️ HATA: Geçersiz giriş! Lütfen sadece sayısal bir değer girin.")

print("--- Program Güvenle Sonlandı ---")