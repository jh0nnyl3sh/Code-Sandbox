from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random


# ----- 1. SETUP ---- 
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

print("Jhony Lesh is riding to Google")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com")

# --- 2. SEARCH -----
time.sleep(random.uniform(2,3))
search_box = driver.find_element(By.NAME, "q")

query = "Python Selenium Documentation" # Hedefkelime
for letter in query:
    search_box.send_keys(letter)
    time.sleep(random.uniform(0.05, 0.2)) # hızlı insan taklidi
    
search_box.send_keys(Keys.RETURN)
print("✅ Search completed. Waiting for results...")

# 3. ---- CLICK ----

time.sleep(3) # sonuçların yüklenmesini bekle (kritik)

# sayfadaki tüm <h3> etiketlerini (başlıkları) bul
results = driver.find_elements(By.CSS_SELECTOR, "h3")

if results:
    print(f"Found {len(results)} results on the first page.")
    print(f"Clicking the first one : '{results[0].text}'")
    
    # ilk sonuca tıkla
    results[0].click()
    
    print("we are inside. check the new url.")
    
else:
    print("No results found or google changed the layout.")


# kapatmadan önce bekle
input("Press Enter to finish the mission...")
driver.quit()