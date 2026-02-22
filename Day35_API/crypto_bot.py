import requests 

def get_crypto_prices():
    # 1. VEZNE ADRESİ (API Endpoint)
    # Burası CoinGecko'nun "Basit Fiyat" sorgualama veznesidir.
    url = "https://api.coingecko.com/api/v3/simple/price"
    
    
    # 2. SİPARİŞ FİŞİ (Parametres)
    # API'ye tam olarak ne istediğimizi söylüyoruz.(Soru işareti ile)
    # URL'ye eklenen kısımlar)
    # "Bana Bitcoin, Ethereum ve Solana'nın USD ve TRY karşılığını ver."
    
    payload = {
        "ids": "bitcoin,ethereum,solana",
        "vs_currencies": "usd,try"
    }
    
    print("📡 [KEYMASTER] CoinGecko API veznesine yaklaşılıyor...")

    # URL'ye fişimizi (params) vererek HTTP GET isteği atıyoruz.
    response = requests.get(url, params=payload)
    
    # Vezne 200 (OK) yanıtı verdiyse işlem başarılıdır.
    if response.status_code == 200:
        
        # 3. SİHİRLİ DOKUNUŞ: JSON ÇEVİRİSİ
        # Gelen veriyi HTML olarak değil, doğrudan Python sözlüğüne (Dictionary) çeviriyoruz!
        data = response.json()
        
        print("✅ [KEYMASTER] Vezneden saf veri alındı.\n")
        
        # --- VERİYİ EKRANA BASTIRALIM ---
        print("📦 GELEN HAM JSON VERİSİ (Sözlük Yapısı) : ")
        print(data)
        print("-" * 40)
        
        
        # 4. VERİYİ AYIKLAMAK (Parsing)
        # Tıpkı C#'taki veya Python'daki sözlüklerden veri çeker gibi : 
        # degisken["anahtar"]["alt_anahtar"]
        btc_usd = data["bitcoin"]["usd"]
        btc_try = data["bitcoin"]["try"]
        eth_usd = data["ethereum"]["usd"]
        eth_try = data["ethereum"]["try"]
        
        btc_try_formatli = f"{btc_try:,}".replace(",",".")
        eth_try_formatli = f"{eth_try:,}".replace(",",".")
        
        print("📊 GÜNCEL PİYASA RAPORU: ")
        print(f"💰 Bitcoin : $ {btc_usd:,} (₺{btc_try_formatli:})")
        print(f"💰 Ethereum : $ {eth_usd:,} (₺{eth_try_formatli:})")
    
    else:
        print(f"❌ [KEYMASTER] Vezne reddetti! Hata Kodu : {response.status_code}")
        
        
# Dosya doğrudan çalıştırılırsa fonkisyonu tetikle
if __name__ == "__main__":
    get_crypto_prices()