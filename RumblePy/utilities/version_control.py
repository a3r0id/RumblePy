from requests import get
def latestVersion():
    return get("https://raw.githubusercontent.com/a3r0id/RumblePy/main/__version__").text
    
    