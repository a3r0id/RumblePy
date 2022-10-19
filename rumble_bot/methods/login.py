from js2py import eval_js
from requests import post
from rumble_bot.static import Static
from pathlib import Path
from os.path import join as pjoin

def login(self):
    
    self.log("[+] Logging in...")
    self.log("[+] Getting salt")

    r = post(Static.URI.service + "?name=user.get_salts", data={"username": self.username})

    salts = r.json()["data"]["salts"]
    
    self.log("[+] Received Salts: {}".format(salts))   
    
    with open(pjoin(Path(__file__).parent.parent, pjoin("dom_scripts", "md5.js")), 'r') as f:
        js = f.read()

    f = eval_js(js)
    
    self.log("[+] JavaScript Engine Started!")
    self.log("[+] Calculating Hashes, this may take a moment...") 

    password_hashes = f(self.password, salts)
    
    self.log("[+] Hashes Calculated: {}".format(password_hashes))
    
    self.log("[+] Sending Login Request...")
    
    r = post(Static.URI.service + "?name=user.login", data={"username": self.username, "password_hashes": ",".join(password_hashes)}) 
    
    json = r.json()
    
    self.session = None
    
    if json["data"]["session"]:
        self.session = json["data"]["session"]
        self.log("[+] Login Successful! Session: {}".format(self.session))
        
    else:
        self.log("[!] Login Failed!")
        
    return self.session
