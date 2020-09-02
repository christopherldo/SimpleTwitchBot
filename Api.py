import requests
from Settings import CHANNEL

url = "https://tmi.twitch.tv/group/user/{}/chatters".format(CHANNEL)
r = requests.get(url=url)
data = r.json()
extract = ['chatters']
streamer_chatters = {key: data[key]['broadcaster'] for key in extract}
streamer_str = str(streamer_chatters)
mods_chatters = {key: data[key]['moderators'] for key in extract}
mods_str = str(mods_chatters)

streamer = streamer_str[15:-3]
mods = mods_str[14:-3].replace("'", '').split(',')
