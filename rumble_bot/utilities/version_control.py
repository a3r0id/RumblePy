from requests import get
def latestVersion():
    return get("https://raw.githubusercontent.com/hostinfodev/Rumble-Bot/main/__version__").text
    
    