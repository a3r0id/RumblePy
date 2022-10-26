from requests import get
from user_agent import generate_user_agent
from time import sleep

string = "spring registration (not open yet)"

while True:
    headers = {'User-Agent': generate_user_agent()}
    #print("[+] Using headers " + str(headers))
    r = get("https://www.earthboundskills.com/homeschool-program", headers=headers)
    if (string not in r.text):
        print("[+] REGISTRATION OPEN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else: 
        print("[-] Not open")
    sleep(30)