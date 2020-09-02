import os
from os.path import isfile
import codecs

try:
    os.mkdir('twitchbotDataFiles')
    print('Directory "twitchbotDataFiles" created.')
except FileExistsError:
    print('Directory "twitchbotDataFiles" already exists.')

if not isfile("twitchbotDataFiles/config.txt"):
    print('Creating file "config.txt"...')
    config = codecs.open("twitchbotDataFiles/config.txt", 'a', 'utf-8')
    config.close()
    config = open("twitchbotDataFiles/config.txt", "a", encoding='utf-8')
    config.write('{}\n{}\n{}\n{}\n{}\n{}\n'.format('irc.twitch.tv', '6667', 'oauth:YOUROAUTHPASS', 'YOURBOTNICK',
                                                   'YOURCHANNEL', 'YOURBOTPASSWORD'))
    config.close()
    print('File "config.txt" created. Please adjust your details then start again')
    exit()

from Api import mods
from Initialize import join_room
from Send import send_message
from Settings import CHANNEL
from Socket import open_socket
from time import sleep


def server_reconnect():
    connected = False
    print('Connection lost.')
    while not connected:
        try:
            client_socket = open_socket()
            client_socket.send("PING :tmi.twitch.tv\r\n".encode("utf-8"))
            connected = True
            print('Re-connected successfully!')
            return client_socket
        except:
            print('Trying to re-connect...')
            sleep(2)


os.system('mode 60,20')

print('\nHi, {}!'.format(CHANNEL))
print('Online mods: {}\n'.format(mods))
print('Bot started!\n')

s = open_socket()
join_room(s)

read_buffer = ''

# message = "/me is online and ready to be used! BloodTrail".format(IDENTITY)
# message_temp = f"PRIVMSG #" + CHANNEL + " :" + message + "\r\n"
# s.send(message_temp.encode('utf-8'))

if not isfile("twitchbotDataFiles/prefix.txt"):
    prefix = codecs.open("twitchbotDataFiles/prefix.txt", 'a', 'utf-8')
    prefix.close()
    prefix = open("twitchbotDataFiles/prefix.txt", "a", encoding='utf-8')
    prefix.write('{}\n'.format('#'))
    prefix.close()

if not isfile("twitchbotDataFiles/jokes_list.txt"):
    jokes_txt = codecs.open("twitchbotDataFiles/jokes_list.txt", 'a', 'utf-8')
    jokes_txt.close()
    jokes_txt = open("twitchbotDataFiles/jokes_list.txt", 'a', encoding='utf-8')
    jokes_txt.write('{}\n'.format('tell me a joke'))
    jokes_txt.close()

commands_list = codecs.open("twitchbotDataFiles/commands_list.txt", 'a', "utf-8")
commands_list.close()
autoreply_list = codecs.open("twitchbotDataFiles/autoreply_list.txt", 'a', 'utf-8')
autoreply_list.close()
owners_list = codecs.open("twitchbotDataFiles/owners_list.txt", 'a', 'utf-8')
owners_list.close()

while True:
    try:
        read_buffer = read_buffer + s.recv(2048).decode('utf-8')
    except:
        s = server_reconnect()
    if read_buffer == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        s.send("PING :tmi.twitch.tv\r\n".encode("utf-8"))
    temp = read_buffer.split('\n')
    read_buffer = temp.pop()

    for line in temp:
        send_message(line, s)
