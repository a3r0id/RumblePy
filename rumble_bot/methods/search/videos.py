from rumble_bot.scraper.Scraper import Scraper
from rumble_bot.Static import Static

def videos(self, query):
    
    scraper = Scraper(
        Static.URI.base + "/search/video?q=" + query,
        cookies={"u_s": self.ctx.session},
        headers=Static.Request.base_headers()
    )
    scraper.scrape()   
    
    videos = []
    
    for video in scraper.soup.find_all("li", class_="video-listing-entry"):
        title = video.find("h3", class_="video-item--title").text
        slug = video.find("a", class_="video-item--a")["href"].split("/")[-1]
        thumbnail = video.find("img", class_="video-item--img")["src"]
        channel = video.find("div", class_="ellipsis-1").text
        duration = video.find("span", class_="video-item--duration")["data-value"]
        views = video.find("span", class_="video-item--views")["data-value"]
        rumbles = video.find("span", class_="video-item--rumbles")["data-value"]
        time = video.find("time", class_="video-item--time")["datetime"]
        
        videos.append({
            "title": title,
            "slug": slug,
            "thumbnail": thumbnail,
            "channel": channel,
            "duration": duration,
            "views": views,
            "rumbles": rumbles,
            "time": time
        })
        
    return videos
    
    