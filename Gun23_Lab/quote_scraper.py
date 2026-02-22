import requests
from bs4 import BeautifulSoup # The soup spoon

# 1. Target url
url = "http://quotes.toscrape.com/"

print(f"🌍 Connecting to {url} ...")

# 2. Get the HTML (Sayfayı indir)
response = requests.get(url)

if response.status_code == 200:
    print("✅ Connection Successful! Parsing HTML...")

    # 3. Create Soup Object 
    # HTML kodlarını Python'un anlayacağı bir nesneye çevir.
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 4. Find Elements (Elementleri bul)
    # Sitede her söz, <div class="quote"> kutusunun içindedir.
    # .find_all() bize bir liste verir.
    quotes = soup.find_all("div", class_="quote")

    print(f"Found {len(quotes)} quotes on this page.\n")
    
    # 5. Loop Through and Extract Data (Döngü ve Veri Çıkarma)
    for item in quotes:
        # Alıntıyı bul (span etiketi, class='text')
        text = item.find("span", class_="text").text
        
        # Yazarı bul (small etiketi, class='author')
        author = item.find("small", class_="author").text
        
        # Ekrana bas
        print(f" Quote : {text}")
        print(f" Author : {author}")
        print("-" * 50)

else:
    print(f"❌ Failed to connect. Status Code : {response.status_code}")