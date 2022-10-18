from js2py import eval_js
from requests import post
from rumble_bot.static import Static

def login(self, email_or_username, password):
    
    self.log("[+] Logging in...")
    self.log("[+] Getting salt")

    r = post(Static.URI.service + "?name=user.get_salts", data={"username": email_or_username})

    salts = r.json()["data"]["salts"]
    
    self.log("[+] Received Salts: {}".format(salts))   

    with open('dom_scripts/md5.js', 'r') as f:
        js = f.read()

    f = eval_js(js)
    
    self.log("[+] JavaScript Engine Started!")
    self.log("[+] Calculating Hashes, this may take a moment...") 

    password_hashes = f(password, salts)
    
    self.log("[+] Hashes Calculated: {}".format(password_hashes))
    
    self.log("[+] Sending Login Request...")
    
    r = post(Static.URI.service + "?name=user.login", data={"username": email_or_username, "password_hashes": ",".join(password_hashes)}) 
    
    json = r.json()
    if json["data"]["session"]:
        self.session = json["data"]["session"]
        self.log("[+] Login Successful! Session: {}".format(self.session))
        
    else:
        self.log("[!] Login Failed!")
        exit(1)
