import bs4
from requests import get
#from brotli import decompress as brotli_decompress

from RumblePy.Static import Static

class Scraper(object):
    
    def __init__(self, url, headers={}, cookies={}, overwrite_user_agent=True):
        self.url      = url
        self.soup     = None
        self.html     = None
        self.response = None
        self.headers  = headers
        
        if overwrite_user_agent:
            self.headers["User-Agent"] = Static.Request.user_agent
        
        self.cookies = cookies
        
    def scrape(self):
        try:
            self.response = get(self.url, headers=self.headers, cookies=self.cookies)
            self.html    = self.response.text

            """
            if "Content-Encoding" in self.response.headers:
                if self.response.headers["Content-Encoding"] == "br":
                    self.html = brotli_decompress(self.response.content).decode("utf-8")
            """

            self.soup    = bs4.BeautifulSoup(self.response.text, 'html.parser')
            return self.soup
        except Exception as e:
            print(e)
        return False
    
    def links(self):
        return [link.get('href') for link in self.soup.find_all('a')]