from RumblePy.scraper.Scraper import Scraper
from RumblePy.Static import Static

def channels(self, query):
    
    scraper = Scraper(
        Static.URI.base + "/search/channel?q=" + query,
        cookies={"u_s": self.ctx.session},
        headers=Static.Request.base_headers()
    )
    scraper.scrape()   
    
    channels = []
    
    for channel in scraper.soup.find_all("li", class_="video-listing-entry"):
        # get the channel name
        name = channel.find("h3", class_="channel-item--title").text
        # get the channel slug
        slug = channel.find("a", class_="channel-item--a")["href"].split("/")[-1]
        # get the channel subscribers
        subscribers = channel.find("span", class_="channel-item--subscribers").text
        
        # TODO: get the channel thumbnail / always None for now...
        #thumbnail = channel.find("div", class_="channel-item--img").find("i")["class"][2].split("--")[-1]
        thumbnail = None
        
        # add the channel to the list
        channels.append({
            "name": name,
            "slug": slug,
            "subscribers": subscribers,
            "thumbnail": thumbnail
        })
        
    return channels
    
    