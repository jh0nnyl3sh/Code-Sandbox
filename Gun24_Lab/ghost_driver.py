from  selenium import webdriver
import time

print(" Jhony Lesh is taking over the browser...")

# 1. Launch Chrome (tarayıcıyı başlat)
# Bu satır çalıştığında ekranda yeni bir chrome penceresi açılacak.
driver = webdriver.Chrome()

# 2. go to target 
url = "https://www.google.com"
driver.get(url)

print(f"✅ Successfully opened: {driver.title}")


# 3. Keep it open for a while (Biraz bekle)
# Eğer bunu koymazsak, Python işi bitti sanıp tarayıcıyı anında kapatır.
time .sleep(5)

print("👋 Closing the browser now...")