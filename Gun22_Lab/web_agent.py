import requests  # Import the library

# Target URL
url = "https://api.github.com"

print(f"Connecting to {url} ...")

# Send GET Request 
response = requests.get(url)


# Check Status 
if response.status_code == 200:
    print("✅ Connection Successful!")
    print("-" * 30)
    print("Server Response Headers: ")
    
    server_info = response.headers.get("Server")
    print(f"Server Software: {server_info}")
    
    
else:
    print(f"❌ Failed! Status Code : {response.status_code}")