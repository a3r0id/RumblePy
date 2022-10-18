from requests import post
from rumble_bot.static import Static

def subscribe(self, slug, title):
    return post(
        Static.URI.service + "?name=user.subscribe",
        data={
            "slug": slug,
            "title": title,
            "type": "channel",
            "action": "subscribe"
        }, cookies={"u_s": self.session}
    ).json()