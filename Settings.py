settings_list = open("twitchbotDataFiles/config.txt", 'r', encoding='utf-8')
settings = list(map(str.strip, settings_list))
settings_list.close()

HOST = settings[0].lower()
PORT = int(settings[1])
PASS = settings[2]
IDENTITY = settings[3].lower()
CHANNEL = settings[4].lower()
PASSWORD = settings[5]
