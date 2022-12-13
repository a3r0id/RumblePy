from RumblePy.scraper.Scraper import Scraper
from RumblePy.Static import Static

from datetime import datetime

def videos(self, query, sort=None, date=None, duration=None):

    # sort options: None = relevance, "date", "rumbles", "views"

    # date options: None = all time, "today", "this-week", "this-month", "this-year"

    # duration options: None = all, "short", "long"

    if sort:
        query += "&sort=" + sort
    else:
        sort = ""

    if date:
        query += "&date=" + date
    else:
        date = ""

    if duration:
        query += "&duration=" + duration
    else:
        duration = ""
    
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
        duration = video.find("span", class_="video-item--duration")["data-value"] if video.find("span", class_="video-item--duration") else None
        views = video.find("span", class_="video-item--views")["data-value"] if video.find("span", class_="video-item--views") else None
        rumbles = video.find("span", class_="video-item--rumbles")["data-value"] if video.find("span", class_="video-item--rumbles") else None
        time =  time = datetime.strptime(video.find("time", class_="video-item--time")["datetime"], "%Y-%m-%dT%H:%M:%S%z") if video.find("time", class_="video-item--time") else None

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
    
    