from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options # Ayarlar için gerekli
import time
import random # İnsan taklidi için rastgelelik

# 1. Stealth Settings (Gizlilik Ayarları)
chrome_options = Options()

# Bu komut, "Otomasyon tarafından kontrol ediliyor" uyarısını gizler
chrome_options.add_argument("--disable-blink-features=AutomationControlled") 

# Tarayıcıyı "headless" (görünmez) yapma, görelim ne oluyor.
# chrome_options.add_argument("--headless") 

# Logları temizle (Gereksiz hata mesajlarını gizle)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

print("🥷 Stealth Mode Activated...")
driver = webdriver.Chrome(options=chrome_options)

# 2. Go to Google
driver.get("https://www.google.com")

# 3. Act like a Human (İnsan Taklidi)
time.sleep(random.uniform(2, 4)) # 2 ile 4 saniye arası rastgele bekle

search_box = driver.find_element(By.NAME, "q")

# Yazıyı harf harf yazıyormuş gibi yapalım (Çok etkili bir yöntemdir)
query = "Python Bug Hunter Jhonny Lesh"
for letter in query:
    search_box.send_keys(letter)
    time.sleep(random.uniform(0.1, 0.3)) # Her harf arası minik bekleme

time.sleep(1)
search_box.send_keys(Keys.RETURN)

print("💥 Search executed with human-like behavior.")

input("🛑 Press Enter to close...")
driver.quit()