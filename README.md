
# RumbleBot
*Unofficial Python wrapper for automating a Rumble account (Rumble.com).*
* This proof-of-concept is a work in progress, and is primitive at best.
* In no way am I affiliated with Rumble.com.
* This is not intended for public use and I am not responsible for any damage caused by this software.

## Example: 
```py
from rumble_bot import RumbleBot

r = RumbleBot(authCfg="config/auth.cfg")

r.login()

print(r.session)
```
            
## Methods:

#### *[`RumbleBot.login(self, email_or_username, password)`](#login)*
> Login to Rumble.com. This must be called on the instance before use of all other [authenticated] methods.
#### *[`RumbleBot.comment(self, postId, text)`](#comment)*
> Comment on a video/post specified by `postId`.
#### *[`RumbleBot.subscribe(self, slug, title)`](#subscribe)*
> Subscribe to a channel specified by `slug` and `title` (???).
#### *[`RumbleBot.vote(self, postId, vote)`](#vote)*
> Upvote/Downvote on a video/post specified by `postId`. `vote` must be either `1` (upvote) or `-1` (downvote).