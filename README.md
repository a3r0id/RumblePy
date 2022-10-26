
# RumbleBot
*Unofficial Python wrapper for automating a Rumble account (Rumble.com).*
* This is a work in progress, and is primitive at best.
* RumbleBot is a self-botting framework and acts as a user-account, not to be confused with the functionality of Rumble.com's [Official Admin/Editor API](https://help.rumble.com/).
* In no way am I affiliated with Rumble.com.
* This is not intended for public use and I am not responsible for any damage caused by the use this software.
* This is not a political project, I simply enjoy reverse engineering social media apps and Rumble has been a very easy platform to do so.

## Example: 
```py
from rumble_bot import RumbleBot

r = RumbleBot(authCfg="config/auth.cfg", opts={"verbose": True})
#r = RumbleBot(username="USERNAME_OR_EMAIL", password="PASSWORD", opts={"verbose": True})

r.login()

print(r.session)

print(r.feeds.subscriptions())


```
            
## Methods:

#### *[`RumbleBot.login(self)`](#login)*
> Login to Rumble.com. This must be called on the instance before use of all other [authenticated] methods.
#### *[`RumbleBot.comment(self, postId, text)`](#comment)*
> Comment on a video/post specified by `postId`.
#### *[`RumbleBot.subscribe(self, slug, title)`](#subscribe)*
> Subscribe to a channel specified by `slug` and `title` (???).
#### *[`RumbleBot.vote(self, postId, vote)`](#vote)*
> Upvote/Downvote on a video/post specified by `postId`. `vote` must be either `1` (upvote) or `-1` (downvote).
#### *[`RumbleBot.feeds.featured_channels(self)`](#featured_channels)*
> Fetch featured channels from Rumble.com's homepage.
#### *[`RumbleBot.feeds.subscriptions(self, page=0)`](#subscriptions)*
> Fetch your feed from Rumble.com's homepage.
## Project Goals:

- [ ] **Feature Request:** Search for posts, users, tags
- [ ] **Feature Request:** Video downloader
- [ ] **Feature Request:** Post a new post
- [ ] **Feature Request:** Reply to nested comments
- [ ] **Feature Request:** Delete a comment, reply or post
- [ ] **Feature Request:** Async!