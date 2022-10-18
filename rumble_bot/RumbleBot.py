from rumble_bot.methods.login     import login
from rumble_bot.methods.comment   import comment
from rumble_bot.methods.vote      import vote
from rumble_bot.methods.subscribe import subscribe
from rumble_bot.static import Static

class RumbleBot(object):
    def __init__(self, username=None, password=None, authCfg=None, opts={}):
        
        self.username = username
        self.password = password
        self.authCfg  = authCfg
        self.session  = None
        
        if self.authCfg:
            with open(self.authCfg, 'r') as f:
                self.username, self.password = [line.strip() for line in f.readlines()]
                
        if "verbose" not in opts:
            opts["verbose"] = False
            
        if "proxy" not in opts:
            opts["proxy"] = None
        
        self.login      = login
        self.login.__setattr__("__doc__", "Login to Rumble.com. This must be called on the instance before use of all other [authenticated] methods.")
        
        self.comment    = comment
        self.comment.__setattr__("__doc__", "Comment on a video/post specified by `postId`.")
        
        self.vote       = vote
        self.vote.__setattr__("__doc__", "Upvote/Downvote on a video/post specified by `postId`. `vote` must be either `1` (upvote) or `-1` (downvote).")
        
        self.subscribe  = subscribe
        self.subscribe.__setattr__("__doc__", "Subscribe to a channel specified by `slug` and `title` (???).")
        
                
        