from RumblePy.Static import Static
from requests import get

def session_test(session):
    r = get("https://rumble.com/login.php",
        cookies={"u_s": session},
        headers={"User-Agent": Static.Request.user_agent}
    )
    
    title = r.text.split("<title>")[1].split("</title>")[0]

    if "Login" in title:
        return False
    return True