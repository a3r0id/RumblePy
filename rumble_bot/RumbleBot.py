from rumble_bot.Static import Static

class RumbleBot(object):    
    def __init__(self, username=None, password=None, authCfg=None, opts={}): 
        
        self.username = username
        self.password = password
        self.authCfg  = authCfg
        self.session  = None
        self.opts     = opts
        
        if self.authCfg:
            with open(self.authCfg, 'r') as f:
                self.username, self.password = [line.strip() for line in f.readlines()]
                
        if "verbose" not in opts:
            opts["verbose"] = False
            
        if "proxy" not in opts:
            opts["proxy"] = None         
        
        # Feeds subclass
        from rumble_bot.methods.feeds.Feeds import Feeds    
        self.feeds = Feeds(self)
        self.feeds.__setattr__("__doc__", "Methods for fetching feeds from Rumble.com.")
        
        # Search subclass
        from rumble_bot.methods.search.Search import Search
        self.search = Search(self)
        self.search.__setattr__("__doc__", "Methods for searching across Rumble.com.")  
        
    from rumble_bot.methods.log       import log
    
    from rumble_bot.methods.login     import login
    login.__setattr__("__doc__", "Login to Rumble.com. This must be called on the instance before use of all other [authenticated] methods.")  
            
    from rumble_bot.methods.comment   import comment
    comment.__setattr__("__doc__", "Comment on a video/post specified by `postId`.")
    
    from rumble_bot.methods.vote      import vote
    vote.__setattr__("__doc__", "Upvote/Downvote on a video/post specified by `postId`. `vote` must be either `1` (upvote) or `-1` (downvote).")        
    
    from rumble_bot.methods.subscribe import subscribe    
    subscribe.__setattr__("__doc__", "Subscribe to a channel specified by `slug` and `title` (???).")   

        
                      
        