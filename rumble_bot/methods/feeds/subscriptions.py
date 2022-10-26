from rumble_bot.scraper.Scraper import Scraper
from rumble_bot.Static import Static

def subscriptions(self, page=0):
    scraper = Scraper(
        Static.URI.base + "/subscriptions?page=" + (str(page) if page > 0 else Static.URI.base + ""),
        cookies={"u_s": self.ctx.session},
        headers={"User-Agent": Static.Request.user_agent}
    )
    
    scraper.scrape()
    
    feed = []
    
    # parse the video info
    """
    <article class="video-item">
        <h3 class="video-item--title">Red Tsunami - In the Litter Box w/ Jewels &amp; Catturd 10/19/2022 - Ep. 192</h3><a
            class="video-item--a"
            href="/v1or4u1-red-tsunami-in-the-litter-box-w-jewels-and-catturd-10192022-ep.-192.html"><img
                class="video-item--img"
                src="https://sp.rmbl.ws/s8/1/5/0/q/f/50qfg.oq1b-small-Red-Tsunami-In-the-Litter-B.jpg"
                alt="Red Tsunami - In the Litter Box w/ Jewels &amp; Catturd 10/19/2022 - Ep. 192"></a>
        <footer class="video-item--footer ellipsis-1">
            <address class="video-item--by"><a rel="author" class="video-item--by-a video-item--by-a--c1313924"
                    href="/c/InTheLitterBox">
                    <div class="ellipsis-1">In The Litter Box w/ Jewels &amp; Catturd<svg
                            class="video-item--by-verified verification-badge-icon" width="24" height="24"
                            viewBox="0 0 24 24">
                            <circle cx="12" cy="12" r="12"></circle>
                            <path fill="none" stroke="currentColor" stroke-width="2" stroke-miterlimit="10"
                                d="M5.4 11.1l5 5 8.2-8.2"></path>
                        </svg></div>
                </a></address><span class="video-item--duration" data-value="1:07:19"></span><span
                class="video-item--meta video-item--views" data-value="6,608"></span><span
                class="video-item--meta video-item--rumbles" data-value="487"></span><time
                class="video-item--meta video-item--time" datetime="2022-10-19T12:26:47-04:00">Oct 19</time>
        </footer>
    </article>
    """
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
    
    