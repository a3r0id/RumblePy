from RumblePy.scraper.Scraper import Scraper

def featured_channels(self):
    scraper  = Scraper('https://rumble.com/')
    scraper.scrape()
    return [dict(
        channel=link.replace("/c/", ""),
        url="https://rumble.com" + link
    ) for link in scraper.links() if "/c/" in link]