class Search(object):
    def __init__(self, ctx):
        self.ctx = ctx
        
    from RumblePy.methods.search.channels import channels
    channels.__setattr__("__doc__", "Search for channels by string.")
    
    from RumblePy.methods.search.videos import videos
    videos.__setattr__("__doc__", "Search for videos by string.")