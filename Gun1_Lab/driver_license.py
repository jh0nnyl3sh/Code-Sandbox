# SABİTLER (CONSTANTS)  : Değişmeyecek değerler büyük harfle yazılır
# (PEP 8 Kuralı).

DRIVER_LİCENSE_AGE = 18
while True:
    try:
        # Girdi ve Dönüştürme
        age_input = input("Yaşınızı Giriniz : ").strip()
        age = int(age_input)
        
        # Mantık Kontrolü (Clean Logic)
        if age >= DRIVER_LİCENSE_AGE:
            print("✅ Ehliyet Alabilirsiniz!")
            break
        
        else:
            # Tek bir matematik işlemi ile sonucu bulmak
            remaining_years = DRIVER_LİCENSE_AGE - age
            print(f"⏳ Ehliyet almak için {remaining_years} yıl daha beklemelisiniz.")
            break
    except ValueError:
        # Kullanıcı sayı yerine "onsekiz" yazarsa program çökmez, uyarır.
        print("❌ Hata: Lütfen yaşınızı rakamla giriniz (Örn: 25). ")