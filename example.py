from RumblePy import RumbleBot

rumble = RumbleBot(authCfg="auth.cfg", opts={"verbose": True})

"""
    // Auth.cfg: //
    <username>
    <password>

    // User/Pass Alternative: //
    r = RumbleBot(username="USERNAME_OR_EMAIL", password="PASSWORD", opts={"verbose": True})
"""

rumble.login() # User/Pass alternative (slower)

# rumble.login(session="SESSION_ID") # Static session login alternative (faster)

for video in rumble.search.videos("test"):
    print ("Title:")
    print("\t" + video["title"])
    print("Slug:")
    print("\t" + video["slug"])
    print("Thumbnail:")
    print("\t" + video["thumbnail"])
    print("Views:")
    print("\t" + video["views"])
    print("Duration:")
    print("\t" + video["duration"])
    print("Time:")
    print("\t" + str(video["time"]))
    print("Channel:")
    print("\t" + video["channel"])
    print("Rumbles:")
    print("\t" + (video["rumbles"] if video["rumbles"] else "N/A"))
    print()

#print(rumble.search.channels("test"))

#print(rumble.feeds.subscriptions())





