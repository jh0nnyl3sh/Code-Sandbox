import requests


# 1. Setup Target
username = "basdasugur" # -> Github username
url = f"https://api.github.com/users/{username}"

print(f"🕵️‍♀️ Investigating user: {username} ...")
print("-" * 40)

# 2. Send Request 
response = requests.get(url)


# 3. Check Status
if response.status_code == 200:
    print("✅ Target Found! Downloading data ...")
    
    
    # 4. Parse JSON (Veriyi çözümle)
    # Sunucudan gelen karmaşık yazıyı Python Sözlüğüne çevirir.
    profile_data = response.json()
    
    # 5. Extract Specific Info (İstediğimiz bilgileri cımbızla)
    # .get() kullanıyoruz ki veri yoksa hata vermesin.
    my_name = profile_data.get("name")
    my_bio = profile_data.get("bio")
    public_repos = profile_data.get("public_repos")
    followers = profile_data.get("followers")
    location = profile_data.get("location")
    created_at = profile_data.get("created_at")
    
    # 6. Display Report (Raporlar)
    print("\n--- 📄 USER REPORT ---")
    print(f"👤 Name : {my_name}")
    print(f"📝 Bio    : {my_bio}")
    print(f"📍 Location : {location}")
    print(f"📦 Repos : {public_repos}")
    print(f"👥 Followers : {followers}")
    print(f"📅 Created : {created_at}")
    
    print("-" * 40)
    print("🖼️ DOWNLOADING PROFILE PICTURE ...")

    # 1. get the image url
    avatar_url = profile_data.get("avatar_url")

    # 2. check if url exists 
    if avatar_url:
        # send a specific requests for the image
        # .stream=True büyük dosyalar için iyidir ama şimdilik düz yapalım
        image_response = requests.get(avatar_url)
        
        if image_response.status_code == 200:
            # 3. save the file (binary mode 'wb)
            # Dosya adını 'github_avatar.jpg' yapıyoruz
            with open("github_avatar.jpg", "wb") as file:
                # ⚠️ CRITICAL  : Use .content (Binary), NOT .text
                file.write(image_response.content)

            print("✅ Successful! Image saved as 'github_avatar.jpg'")

        else:
            print("❌ Failed to download image.")
else:
    print(f"❌ Error! User not found. Status Code : {response.status_code}")