from rumble_bot import RumbleBot

r = RumbleBot(authCfg="config/auth.cfg", opts={"verbose": True})

r.login()

print(r.session)