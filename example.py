from rumble_bot import RumbleBot

r = RumbleBot(authCfg="config/auth.cfg")

r.login()

print(r.session)