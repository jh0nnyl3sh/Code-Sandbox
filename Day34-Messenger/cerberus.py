import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

# 1. KENDİ YAZDIĞIMIZ MODÜLÜ İÇERİ AKTARIYORUZ (İşte Büyü Burada!)
from scraper import get_adalet_news

load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASS")
RECEIVER = "basdasugur@gmail.com" # Kendine gönder
#RECEIVER = os.getenv("EMAIL_USER") # Kendine gönder

print("🐺 PROJECT CERBERUS BAŞLATILIYOR...\n")

# --- FAZ 1: VERİ TOPLAMA (Scraping) ---
# scraper.py içindeki fonksiyonu çalıştırıyoruz. Bize CSV dosyasının adını verecek.
rapor_dosyasi = get_adalet_news()


# --- FAZ 2: İLETİŞİM (Mailer) ---
if rapor_dosyasi: # Eğer dosya başarıyla oluşturulduysa (None değilse)
    print("\n📨 [MAILER] Rapor hedefe gönderiliyor...")
    
    msg = EmailMessage()
    msg['Subject'] = '🕵️‍♂️ GÜNLÜK İSTİHBARAT: Adalet Bakanlığı Duyuruları'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECEIVER
    msg.set_content("Merhaba Operatör,\n\nBugünkü Adalet Bakanlığı duyuru taraması tamamlandı. En güncel rapor ektedir.\n\nSaygılar,\nCerberus Bot 🐺")

    # Dosyayı Ekle
    with open(rapor_dosyasi, 'rb') as f:
        file_data = f.read()
    msg.add_attachment(file_data, maintype='text', subtype='csv', filename=rapor_dosyasi)

    # Gönder
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("✅ [MAILER] GÖREV BAŞARILI! Mail eklentiyle birlikte gönderildi.")
    except Exception as e:
        print(f"❌ [MAILER] Mail gönderim hatası: {e}")
else:
    print("⚠️ Operasyon iptal edildi. Veri çekilemediği için mail atılmıyor.")