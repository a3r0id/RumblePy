from RumblePy.scraper.Scraper import Scraper
from RumblePy.Static import Static

def subscriptions(self, page=0):
    scraper = Scraper(
        Static.URI.base + "/subscriptions?page=" + (str(page) if page > 0 else Static.URI.base + ""),
        cookies={"u_s": self.ctx.session},
        headers={"User-Agent": Static.Request.user_agent}
    )
    
    scraper.scrape()
    
    feed = []
    
    for article in scraper.soup.find_all("article", class_="video-item"):
        # get the video title
        title = article.find("h3", class_="video-item--title").text
        # get the video slug
        slug = article.find("a", class_="video-item--a")["href"].split("/")[-1]
        # get the video thumbnail
        thumbnail = article.find("img", class_="video-item--img")["src"]
        # get the video channel
        channel = article.find("div", class_="ellipsis-1").text
        # get the video duration
        duration = article.find("span", class_="video-item--duration")["data-value"]
        # get the video views
        views = article.find("span", class_="video-item--views")["data-value"]
        # get the video rumbles
        rumbles = article.find("span", class_="video-item--rumbles")["data-value"]
        # get the video time
        time = article.find("time", class_="video-item--time")["datetime"]
        
        # add the video to the feed
        feed.append({
            "title": title,
            "slug": slug,
            "thumbnail": thumbnail,
            "channel": channel,
            "duration": duration,
            "views": views,
            "rumbles": rumbles,
            "time": time
        })
        
    return {
        "page": page,
        "feed": feed
    }
    
    