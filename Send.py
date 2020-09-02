from Read import get_user, get_message
import Commands
from Settings import IDENTITY
from datetime import datetime


def send_message(line, s):
    time = datetime.now()
    user = get_user(line)
    message = str(get_message(line)).strip()
    if 'tmi.twitch.tv' not in user and IDENTITY not in user:
        ascii_message = message
        print(time.strftime("%H:%M:%S ") + user + ': ' + ascii_message.encode('ascii', 'replace').decode())
        Commands.commands_request(user, message, s)
