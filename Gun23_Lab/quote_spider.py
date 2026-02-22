import requests
from bs4 import BeautifulSoup
import time
import csv  # Excel formatı için kütüphane

# Setup
page_number = 1
base_url = "http://quotes.toscrape.com"
filename = "quotes_database.csv"

# 1. Create CSV File & Write Headers (Dosyayı Oluştur ve Başlıkları Yaz)
# 'w' modu dosyayı sıfırdan oluşturur.
with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"]) # Başlık Satırı

print(f"🕷️ SPIDER ACTIVATED! Saving data to {filename}...")
print("-" * 50)

while True:
    target_url = f"{base_url}/page/{page_number}/"
    print(f"📂 Scraping Page {page_number}...")
    
    response = requests.get(target_url)
    
    if response.status_code != 200:
        break # Hata varsa dur
        
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")
    
    # 2. Append Data to CSV (Veriyi Ekleyerek Git)
    # 'a' (append) modu ile açıyoruz ki eski veriler silinmesin.
    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        for item in quotes:
            text = item.find("span", class_="text").text
            author = item.find("small", class_="author").text
            
            # Write row (Satırı yaz)
            writer.writerow([text, author])

    # 3. Pagination Logic
    next_button = soup.find("li", class_="next")
    
    if next_button:
        page_number += 1
        time.sleep(1) # Be polite!
    else:
        print("\n✅ End of pages. Crawl complete!")
        break

print("-" * 50)
print(f"🎉 SUCCESS! All data saved in '{filename}'")