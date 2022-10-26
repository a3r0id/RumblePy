from rumble_bot import RumbleBot

r = RumbleBot(authCfg="config/auth.cfg", opts={"verbose": True})
#r = RumbleBot(username="USERNAME_OR_EMAIL", password="PASSWORD", opts={"verbose": True})

r.login()

print(r.session)

print(r.feeds.subscriptions())

