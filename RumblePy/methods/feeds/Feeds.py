class Feeds(object):
    def __init__(self, ctx):
        self.ctx = ctx
        
    from RumblePy.methods.feeds.featured_channels import featured_channels
    featured_channels.__setattr__("__doc__", "Fetch featured channels from Rumble.com's homepage.")
    
    from RumblePy.methods.feeds.subscriptions import subscriptions
    subscriptions.__setattr__("__doc__", "Fetch your feed from Rumble.com's homepage.")
        
    
    