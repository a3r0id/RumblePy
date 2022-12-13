from datetime import datetime
def log(self, message):
    if self.opts['verbose']:
        print("[{}] {}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), message))