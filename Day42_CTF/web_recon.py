import requests

def http_scanner(hedef):
    # Dışarıdan gelen hedefi 'f-string' ile URL'nin içine yerleştiriyoruz
    url = f"http://{hedef}"

    print(f"📡 '{url}' adresine bağlanılıyor.")
    
    try:
        # 2. İSTEK GÖNDER (Timeout ekledik ki sonsuza kadar beklemesin)
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            print("✅ Bağlantı Başarılı! Veri Alındı!")
            
            # MİMARIN BONUSU: Hedefin sunucu kimliğini (Header) çekiyoruz
            sunucu_kimligi = response.headers.get("Server", "Gizlenmiş")
            print(f"    - Sunucu Teknolojisi: {sunucu_kimligi}\n")
            
    except requests.exceptions.RequestException:
        print("❌ Web katmanına ulaşılamadı. Sunucu HTTP isteklerini reddediyor.")