import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

def send_report(excel_file, image_file, receiver_email="basdasugur@gmail.com"):
    print("📧 [EMAIL ENGINE] Raporlar e-posta için hazırlanıyor...")

    
    # Şifreleri .env'den gizlice çekelim
    load_dotenv()
    SENDER_EMAIL = os.getenv("SENDER_EMAIL")
    SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
    

    # 1 MAİL İNŞASI
    msg = EmailMessage()
    msg['Subject'] = "Açık Dosyalar Raporu ve Analizi Grafiği"
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver_email
    msg.set_content("Merhaba\n\nGüncel açık dosyaların Excel dökümü ve tür dağılım grafiği ekte sunulmuştur.\n\nSistem tarafından otomatik oluşturulmuştur.")

    
    # 2. EXCEL DOSYASINI EKE KOYALIM
    # Dosyayı "rb" (read binary - ikili okuma) modunda açıyoruz.
    with open(excel_file, 'rb') as f:
        excel_data = f.read()
        excel_name = os.path.basename(f.name)
        # maintype ve subtype dosyanın formatını belirtir (Excel için bu şekildedir)
        msg.add_attachment(excel_data, maintype='application', subtype="vnd.openxmlformats-officedocument.speardsheetml.sheet", filename=excel_name)

        
    # 3. GRAFİK (PNG) DOSYASINI EKE KOYALIM
    if image_file: # Eğer resim başarıyla gelmişse
        with open(image_file, 'rb') as f:
            image_data = f.read()
            image_name = os.path.basename(f.name)
            msg.add_attachment(image_data, maintype="image", subtype="png", filename=image_name)
            
    
    # 4. GÖNDERİM İŞLEMİ (SMTP)
    try:
        print("🚀 [MAIL ENGINE] Sunucuya bağlanılıyor ve fırlatılıyor...")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
            
        print("✅ [EMAIL ENGINE] Rapor başarıyla hedefe ulaştı!")
        return True
    
    except Exception as e:
        print(f"❌ [EMAIL ENGINE HATA] Gönderim başarısız: {e}")
        return False
    
# Test bloğu
if __name__ == "__main__":
    # Test ederken kendi mailini alıcı olarak yaz
    send_report("Guncel_Acik_Dosyalar.xlsx", "Acik_Dosyalar_Grafigi.png", "basdasugur@gmail.com")