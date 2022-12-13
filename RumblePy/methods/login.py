from js2py import eval_js
from requests import post
from RumblePy.Static import Static
from RumblePy.utilities.session_test import session_test
from pathlib import Path
from os.path import join as pjoin

def login(self, session=None):
    
    self.log("[+] Logging in...")

    # Check if we have a session already
    if session:
        self.log("[+] Session provided, checking...")
        self.session = session
        if session_test(self.session):
            self.log("[+] Session is valid!")
            return self.session
    
        self.log("[+] Invalid session provided, logging in...")

    self.log("[+] Getting salt")

    r = post(Static.URI.service + "?name=user.get_salts", data={"username": self.username}, headers={"User-Agent": Static.Request.user_agent})

    salts = r.json()["data"]["salts"]
    
    self.log("[+] Received Salts: {}".format(salts))   
    
    with open(pjoin(Path(__file__).parent.parent, pjoin("dom_scripts", "md5Ex.js")), 'r') as f:
        js = f.read()

    f = eval_js(js)
    
    self.log("[+] JavaScript Engine Started!")
    self.log("[+] Calculating Hashes, this may take a moment...") 

    password_hashes = f(self.password, salts)
    
    self.log("[+] Hashes Calculated: {}".format(password_hashes))
    
    self.log("[+] Sending Login Request...")
    
    r = post(Static.URI.service + "?name=user.login", data={"username": self.username, "password_hashes": ",".join(password_hashes)}, headers={"User-Agent": Static.Request.user_agent}) 
    
    json = r.json()
    
    self.session = None
    
    if json["data"]["session"]:
        self.session = json["data"]["session"]
        self.log("[+] Login Successful! Session: {}".format(self.session if not self.hide_session else "<HIDDEN>"))
        
    else:
        self.log("[!] Login Failed!")
        
    return self.session
