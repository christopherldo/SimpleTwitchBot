from datetime import datetime


def get_user(line):
    separate = (str(line)).split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user


def get_message(line):
    separate = line.split(":", 2)
    if separate[-1] == 'tmi.twitch.tv\r':
        time = datetime.now()
        if 'PING' in line:
            print('PING requested at: {}'.format(time.strftime("%H:%M:%S %d/%m/%Y")))
        elif 'PONG' in line:
            print('PING sent at: {}'.format(time.strftime("%H:%M:%S %d/%m/%Y")))
            print('PONG received at: {}'.format(time.strftime("%H:%M:%S %d/%m/%Y")))
        return
    elif separate[0] == '':
        try:
            message = separate[2]
        except:
            return
        return message
