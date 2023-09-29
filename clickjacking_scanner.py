import requests
with open("domains.txt","r") as file:
    domains=file.readlines()
print("""
   _____ _ _      _    _            _    _              
  / ____| (_)    | |  (_)          | |  (_)             
 | |    | |_  ___| | ___  __ _  ___| | ___ _ __   __ _  
 | |    | | |/ __| |/ / |/ _` |/ __| |/ / | '_ \ / _` | 
 | |____| | | (__|   <| | (_| | (__|   <| | | | | (_| | 
  \_____|_|_|\___|_|\_\ |\__,_|\___|_|\_\_|_| |_|\__, | 
  / ____|            _/ |                         __/ | 
 | (___   ___ __ _ _|__/ _ __   ___ _ __         |___/  
  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|               
  ____) | (_| (_| | | | | | | |  __/ |                  
 |_____/ \___\__,_|_| |_|_| |_|\___|_|            BY: Ravan Panjaliyev    
                                                        
                                                        
""")
for domain in domains:
    domain=domain.strip()
    try:
        headers=requests.get("http://"+domain).headers    
        if "X-Frame-Options" in headers:
            print(f"{domain} is SECURE to Clickjacking!")
        else:
            print(f"{domain} is VULNERABLE to Clickjacking!")
          
    except requests.exceptions.RequestException:
        print(f"Error: The domain '{domain}' doesn't exist or the connection failed !!!")
