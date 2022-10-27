class Feeds(object):
    def __init__(self, ctx):
        self.ctx = ctx
        
    from rumble_bot.methods.feeds.featured_channels import featured_channels
    featured_channels.__setattr__("__doc__", "Fetch featured channels from Rumble.com's homepage.")
    
    from rumble_bot.methods.feeds.subscriptions import subscriptions
    subscriptions.__setattr__("__doc__", "Fetch your feed from Rumble.com's homepage.")
        
    
    