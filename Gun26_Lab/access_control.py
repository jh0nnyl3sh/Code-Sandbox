# --- AYARLAR (CONSTANTS) ---
MIN_AGE = 18
MAX_AGE = 120

def get_valid_age() -> int:
    """
    Kullanıcıdan geçerli bir yaş (int) değeri alana kadar sorar.
    Sadece rakam ve belirlenen aralıkta (MIN_AGE - MAX_AGE) kabul eder.
    """
    while True:
        user_input = input(f"Lütfen yaşınızı giriniz ({MIN_AGE}-{MAX_AGE}): ").strip()
        
        # 1. Kontrol: Sayısal mı?
        if not user_input.isdigit():
            print("❌ Hata: Giriş sadece rakamlardan oluşmalıdır.")
            continue  # Döngünün başına dön
            
        # 2. Kontrol: Aralık Uygun mu?
        age = int(user_input)
        if MIN_AGE <= age <= MAX_AGE:
            return age  # Geçerli yaşı döndür ve fonksiyonu bitir.
        else:
            print(f"❌ Hata: Yaşınız {MIN_AGE} ile {MAX_AGE} arasında olmalıdır.")

# --- ANA PROGRAM AKIŞI ---
print("--- GÜVENLİK KONTROLÜ BAŞLATILIYOR ---")

# Senior farkı: Artık sadece fonksiyonu çağırıyoruz. Detaylarla boğulmuyoruz.
agent_age = get_valid_age()

print(f"✅ Onaylandı. Sisteme giriş yapılıyor. (Yaş: {agent_age})")