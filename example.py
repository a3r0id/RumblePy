from rumble_bot import RumbleBot

r = RumbleBot(authCfg="auth.cfg", opts={"verbose": True})

"""
// Auth.cfg: //
<username>
<password>

// User/Pass Alternative: //
r = RumbleBot(username="USERNAME_OR_EMAIL", password="PASSWORD", opts={"verbose": True})
"""

r.login()

# r.login(session="SESSION_ID") # Session ID Alternative (faster)

videos = r.search.videos("test")

for video in videos:
    print(video["title"])
    print(video["slug"])
    print(video["thumbnail"])
    print(video["views"])
    print(video["duration"])
    print(video["time"])
    print(video["channel"])
    print(video["rumbles"])
    print()

#print(r.search.channels("test"))

#print(r.feeds.subscriptions())





