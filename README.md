
# RumblePy
*Unofficial Python wrapper for automating a Rumble account (Rumble.com).*
* This is a work in progress, and is primitive at best.
* RumblePy is a self-botting framework and acts as a user-account, not to be confused with the functionality of Rumble.com's [Official Admin/Editor API](https://help.rumble.com/).
* In no way am I affiliated with Rumble.com.
* This is not intended for public use and I am not responsible for any damage caused by the use of this software.
* This is not a political project, I simply enjoy reverse engineering social media apps and Rumble has been a very easy platform to do so.

## Example: 
```py
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






```
            
## Methods:

#### *[`RumbleBot.login(self, session=None)`](#login)*
> Login to Rumble.com. This must be called on the instance before use of all other [authenticated] methods.
#### *[`RumbleBot.comment(self, postId, text)`](#comment)*
> Comment on a video/post specified by `postId`.
#### *[`RumbleBot.delete_comment(self, commentId, isRestore=False)`](#delete_comment)*
> Delete a comment specified by `commentId`. `isRestore` must be either `True` or `False` and will restore a deleted comment if `True`, respective to the `commentId`.
#### *[`RumbleBot.reply(self, postId, commentId, text)`](#reply)*
> Reply to a comment specified by `commentId` under a video/post specified by `postId`.
#### *[`RumbleBot.subscribe(self, slug, title)`](#subscribe)*
> Subscribe to a channel specified by `slug` and `title` (???).
#### *[`RumbleBot.vote(self, postId, vote)`](#vote)*
> Upvote/Downvote on a video/post specified by `postId`. `vote` must be either `1` (upvote) or `-1` (downvote).
#### *[`RumbleBot.feeds.featured_channels(self)`](#featured_channels)*
> Fetch featured channels from Rumble.com's homepage.
#### *[`RumbleBot.feeds.subscriptions(self, page=0)`](#subscriptions)*
> Fetch your feed from Rumble.com's homepage.
#### *[`RumbleBot.search.channels(self, query)`](#channels)*
> Search for channels by string.
#### *[`RumbleBot.search.videos(self, query, sort=None, date=None, duration=None)`](#videos)*
> Search for videos by string.
## Project Goals:

- [ ] **Feature Request:** Post a video
- [ ] **Feature Request:** Async
- [ ] **Feature Request:** Comment enumeration