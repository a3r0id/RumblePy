import bs4
from requests import get
from rumble_bot.Static import Static

class Scraper(object):
    
    def __init__(self, url, headers={}, cookies={}, overwrite_user_agent=True):
        self.url  = url
        self.soup = None
        self.html = None
        self.request = None
        self.headers = headers
        
        if overwrite_user_agent:
            self.headers["User-Agent"] = Static.Request.user_agent
        
        self.cookies = cookies
        
    def scrape(self):
        try:
            self.request = get(self.url, headers=self.headers, cookies=self.cookies)
            self.html    = self.request.text
            self.soup    = bs4.BeautifulSoup(self.request.text, 'html.parser')
            return self.soup
        except Exception as e:
            print(e)
        return False
    
    def links(self):
        return [link.get('href') for link in self.soup.find_all('a')]