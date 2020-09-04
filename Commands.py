from importlib import reload
from random import choice
from Settings import CHANNEL, IDENTITY
from time import sleep

global command, autoreply, joke, prefix, commands_list, autoreply_list, autoreply_in_autoreplies, command_in_commands,\
    joke_in_jokes, prefix_edit, count_command, count_command_save, count_reply, count_reply_save

commands_exclusive = ['command', 'commands', 'autoreply', 'autoreplies', 'prefix', 'joke']
prefix_possibles = ['!', '#', '-', '+']


def write_command(message):
    global command, command_in_commands, commands_list, commands_exclusive, count_command, count_command_save
    command_caller = message.strip()
    command_and_response = command_caller.split(" ", maxsplit=3)
    try:
        command = str(command_and_response[2]).lower()
        response = str(command_and_response[3])
    except:
        command_in_commands = 'Error'
        return
    user_level = 'user'
    old_commands_list = open("twitchbotDataFiles/commands_list.txt", 'r', encoding='utf-8')
    commands = list(map(str.strip, old_commands_list))[0::4]
    old_commands_list.close()
    if command in commands_exclusive:
        command_in_commands = 'Exclusive'
    elif command in commands:
        command_in_commands = 'True'
        command_count_add()
        count_command_save = str(int(count_command) - 1)
    elif command not in commands:
        command_in_commands = 'False'
        commands_list = open("twitchbotDataFiles/commands_list.txt", "a", encoding='utf-8')
        commands_list.write('{}\n{}\n{}\n{}\n'.format(command, response, count_command, user_level))
        commands_list.close()


def write_autoreply(message):
    global autoreply, autoreply_in_autoreplies, autoreply_list, count_reply, count_reply_save
    autoreply_caller = message.strip()
    autoreply_and_response = autoreply_caller.split(" ", maxsplit=3)
    try:
        autoreply = str(autoreply_and_response[2]).lower()
        response = autoreply_and_response[3]
    except:
        autoreply_in_autoreplies = 'Error'
        return
    if "/me" in autoreply:
        autoreply = autoreply.replace("/me", "action")
    autoreply_txt = open("twitchbotDataFiles/autoreply_list.txt", 'r', encoding='utf-8')
    old_autoreply_list = list(map(str.strip, autoreply_txt))
    autoreply_txt.close()
    autoreplies = old_autoreply_list[0::3]
    if autoreply in autoreplies:
        autoreply_in_autoreplies = 'True'
        autoreply_count_add()
        count_reply_save = str(int(count_reply) - 1)
    elif autoreply not in autoreplies:
        autoreply_in_autoreplies = 'False'
        autoreply_list = open("twitchbotDataFiles/autoreply_list.txt", "a", encoding='utf-8')
        autoreply_list.write('{}\n{}\n{}\n'.format(autoreply, response, count_reply))
        autoreply_list.close()


def write_joke(message):
    global joke, joke_in_jokes
    joke_caller = message.strip()
    try:
        joke_and_response = str((joke_caller.split(' ', maxsplit=2))[2]).split('/')
        joke = joke_and_response[0].strip()
        response = joke_and_response[1].strip()
    except:
        joke_in_jokes = 'Error'
        return
    jokes_txt = open("twitchbotDataFiles/jokes_list.txt", 'r', encoding='utf-8')
    old_jokes_list = list(map(str.strip, jokes_txt))
    jokes_txt.close()
    jokes = old_jokes_list[1::2]
    if joke in jokes:
        joke_in_jokes = 'True'
    elif joke not in jokes:
        joke_in_jokes = 'False'
        jokes_txt = open("twitchbotDataFiles/jokes_list.txt", 'a', encoding='utf-8')
        jokes_txt.write('{}\n{}\n'.format(joke, response))


def delete_command(message):
    global command, command_in_commands, commands_exclusive
    command_caller = message.strip()
    command_and_response = command_caller.split(" ", maxsplit=3)
    try:
        command = command_and_response[2].lower()
    except:
        command_in_commands = 'Error'
        return
    old_commands_list = open("twitchbotDataFiles/commands_list.txt", 'r', encoding='utf-8')
    commands = list(map(str.strip, old_commands_list))[0::4]
    old_commands_list.close()
    if command in commands_exclusive:
        command_in_commands = 'Exclusive'
    elif command not in commands:
        command_in_commands = 'False'
    elif command in commands:
        command_in_commands = 'True'
        old_commands_list = open("twitchbotDataFiles/commands_list.txt", "r", encoding='utf-8')
        lines = old_commands_list.readlines()
        old_commands_list.close()
        current_command = command
        commands_position = (commands.index(current_command) + 1) * 4 - 3

        del lines[commands_position - 1]

        new_commands_list = open("twitchbotDataFiles/commands_list.txt", "w", encoding='utf-8')
        for line in lines:
            new_commands_list.write(line)
        new_commands_list.close()

        del lines[commands_position - 1]

        new_commands_list = open("twitchbotDataFiles/commands_list.txt", "w", encoding='utf-8')
        for line in lines:
            new_commands_list.write(line)
        new_commands_list.close()

        del lines[commands_position - 1]

        new_commands_list = open("twitchbotDataFiles/commands_list.txt", "w", encoding='utf-8')
        for line in lines:
            new_commands_list.write(line)
        new_commands_list.close()

        del lines[commands_position - 1]

        new_commands_list = open("twitchbotDataFiles/commands_list.txt", "w", encoding='utf-8')
        for line in lines:
            new_commands_list.write(line)
        new_commands_list.close()


def delete_autoreply(message):
    global autoreply, autoreply_in_autoreplies
    autoreply_caller = message.strip()
    autoreply_and_response = autoreply_caller.split(" ", maxsplit=3)
    try:
        autoreply = autoreply_and_response[2].lower()
    except:
        autoreply_in_autoreplies = 'Error'
        return
    autoreply_txt = open("twitchbotDataFiles/autoreply_list.txt", 'r', encoding='utf-8')
    old_reply_list = list(map(str.strip, autoreply_txt))
    autoreply_txt.close()
    autoreplies = old_reply_list[0::3]
    if autoreply not in autoreplies:
        autoreply_in_autoreplies = 'False'
    elif autoreply in autoreplies:
        autoreply_in_autoreplies = 'True'
        old_autoreply_list = open("twitchbotDataFiles/autoreply_list.txt", "r", encoding='utf-8')
        lines = old_autoreply_list.readlines()
        old_autoreply_list.close()
        current_autoreply = autoreply + '\n'
        autoreply_position = (lines.index(current_autoreply))

        del lines[autoreply_position]

        new_autoreply_list = open("twitchbotDataFiles/autoreply_list.txt", "w", encoding='utf-8')
        for line in lines:
            new_autoreply_list.write(line)
        new_autoreply_list.close()

        del lines[autoreply_position]

        new_autoreply_list = open("twitchbotDataFiles/autoreply_list.txt", "w", encoding='utf-8')
        for line in lines:
            new_autoreply_list.write(line)
        new_autoreply_list.close()

        del lines[autoreply_position]

        new_autoreply_list = open("twitchbotDataFiles/autoreply_list.txt", "w", encoding='utf-8')
        for line in lines:
            new_autoreply_list.write(line)
        new_autoreply_list.close()


def prefix_edition(message):
    global prefix, prefix_edit, prefix_possibles
    prefix_edit_caller = message.strip()
    try:
        new_prefix = str((prefix_edit_caller.split(' ', maxsplit=3))[2])
    except:
        prefix_edit = 'None'
        return
    if prefix_edit_caller.split(' ')[1] != 'edit' or len(new_prefix) > 1:
        prefix_edit = 'Error'
    elif new_prefix not in prefix_possibles:
        prefix_edit = 'WrongSymbol'
    else:
        prefix = new_prefix
        old_prefix_list = open("twitchbotDataFiles/prefix.txt", 'w', encoding='utf-8')
        old_prefix_list.write(new_prefix + '\n')
        old_prefix_list.close()
        prefix_edit = 'True'


def command_count_add():
    global command, count_command
    old_commands_list = open("twitchbotDataFiles/commands_list.txt", 'r', encoding='utf-8')
    commands = list(map(str.strip, old_commands_list))[0::4]
    old_commands_list.close()
    command_position = (commands.index(command) + 1) * 4 - 3
    count_position = command_position + 2
    old_commands_list = open("twitchbotDataFiles/commands_list.txt", 'r', encoding='utf-8')
    list_of_lines = old_commands_list.readlines()
    old_commands_list.close()
    count_current = list_of_lines[count_position - 1]
    list_of_lines[count_position - 1] = str(int(count_current) + 1) + '\n'
    old_commands_list.close()
    old_commands_list = open("twitchbotDataFiles/commands_list.txt", 'w', encoding='utf-8')
    old_commands_list.writelines(list_of_lines)
    old_commands_list.close()
    count_command = str(int(count_current) + 1)


def autoreply_count_add():
    global autoreply, count_reply
    old_reply_list = open("twitchbotDataFiles/autoreply_list.txt", 'r', encoding='utf-8')
    autoreplies = list(map(str.strip, old_reply_list))[0::3]
    old_reply_list.close()
    autoreply_position = (autoreplies.index(autoreply) + 1) * 3 - 2
    count_position = autoreply_position + 2
    old_reply_list = open("twitchbotDataFiles/autoreply_list.txt", 'r', encoding='utf-8')
    list_of_lines = old_reply_list.readlines()
    old_reply_list.close()
    count_current = list_of_lines[count_position - 1]
    list_of_lines[count_position - 1] = str(int(count_current) + 1) + '\n'
    old_reply_list.close()
    old_reply_list = open("twitchbotDataFiles/autoreply_list.txt", 'w', encoding='utf-8')
    old_reply_list.writelines(list_of_lines)
    old_reply_list.close()
    count_reply = str(int(count_current) + 1)


def get_autoreply(message, autoreply_anywhere):
    for i in range((len(autoreply_anywhere))):
        if autoreply_anywhere[i] in message.lower():
            word = autoreply_anywhere[i]
            return word


def commands_request(user, message, s):
    import Api
    reload(Api)
    import Api
    mods = Api.mods

    global command, command_in_commands, autoreply, autoreply_in_autoreplies, joke, joke_in_jokes, \
        prefix, prefix_edit, count_reply, count_command, count_reply_save, count_command_save

    prefix_file = open("twitchbotDataFiles/prefix.txt", 'r', encoding='utf-8')
    prefix = list(map(str.strip, prefix_file))[0]
    prefix_file.close()
    owners_list = open("twitchbotDataFiles/owners_list.txt", 'r', encoding='utf-8')
    owners = list(map(str.strip, owners_list))
    owners_list.close()

    if user == CHANNEL or user in mods or user in owners:
        if message.lower().startswith(prefix+'command'):
            if message.lower().startswith(prefix+'command add'):
                count_command = '0'
                write_command(message)
                if command_in_commands == 'True':
                    delete_command(message)
                    count_command = count_command_save
                    write_command(message)
                    message = '/me The command was modified.'
                elif command_in_commands == 'False':
                    message = '/me The command "{}" was added.'.format(command)
                elif command_in_commands == 'Error':
                    message = '/me Incorrect Parameter.'
                elif command_in_commands == 'Exclusive':
                    message = '/me This command is exclusive.'
                message_temp = f"PRIVMSG #" + CHANNEL + " :" + message + "\r\n"
                s.send(message_temp.encode('utf-8'))
                print('{}: {}'.format(IDENTITY, message.encode('ascii', 'replace').decode()))
                return
            elif message.lower().startswith(prefix+'command delete'):
                delete_command(message)
                if command_in_commands == 'False':
                    message = '/me This command does not exist'
                elif command_in_commands == 'True':
                    message = '/me The command "{}" was deleted.'.format(command)
                elif command_in_commands == 'Error':
                    message = '/me Incorrect Parameter.'
                elif command_in_commands == 'Exclusive':
                    message = '/me This command is exclusive and can not be deleted.'.format(command)
                message_temp = f"PRIVMSG #" + CHANNEL + " :" + message + "\r\n"
                s.send(message_temp.encode('utf-8'))
                print('{}: {}'.format(IDENTITY, message.encode('ascii', 'replace').decode()))
                return
        elif message.lower().startswith(prefix+'autoreply'):
            if message.lower().startswith(prefix+'autoreply add'):
                count_reply = '0'
                write_autoreply(message)
                if autoreply_in_autoreplies == 'True':
                    delete_autoreply(message)
                    count_reply = count_reply_save
                    write_autoreply(message)
                    message = '/me The autoreply was modified.'
                elif autoreply_in_autoreplies == 'False':
                    message = '/me The autoreply was added.'
                elif autoreply_in_autoreplies == 'Error':
                    message = '/me Incorrect Parameter.'
                message_temp = f"PRIVMSG #" + CHANNEL + " :" + message + "\r\n"
                s.send(message_temp.encode('utf-8'))
                print('{}: {}'.format(IDENTITY, message.encode('ascii', 'replace').decode()))
                return
            elif message.lower().startswith(prefix+'autoreply delete'):
                delete_autoreply(message)
                if autoreply_in_autoreplies == 'False':
                    message = '/me This autoreply does not exist.'
                elif autoreply_in_autoreplies == 'True':
                    message = '/me The autoreply "{}" was deleted.'.format(autoreply)
                elif autoreply_in_autoreplies == 'Error':
                    message = '/me Incorrect Parameter.'
                message_temp = f"PRIVMSG #" + CHANNEL + " :" + message + "\r\n"
                s.send(message_temp.encode('utf-8'))
                print('{}: {}'.format(IDENTITY, message.encode('ascii', 'replace').decode()))
                return
        elif message.lower().startswith(prefix+'joke add'):
            write_joke(message)
            if joke_in_jokes == 'False':
                message = '/me The joke was added.'
            elif joke_in_jokes == 'Error':
                message = '/me Incorrect Parameter'
            message_temp = f"PRIVMSG #" + CHANNEL + " :" + message + "\r\n"
            s.send(message_temp.encode('utf-8'))
            print('{}: {}'.format(IDENTITY, message.encode('ascii', 'replace').decode()))
            return
        elif any(prefix in prefix_possibles for prefix in message.lower()[0]):
            if message.lower()[0] != prefix:
                if message.lower()[1:7] == 'prefix':
                    message = '/me The prefix is: "{}"'.format(prefix)
                    message_temp = f"PRIVMSG #" + CHANNEL + " :" + message + "\r\n"
                    s.send(message_temp.encode('utf-8'))
                    print('{}: {}'.format(IDENTITY, message.encode('ascii', 'replace').decode()))
                    return
            elif message.lower().startswith(prefix+'prefix'):
                prefix_edition(message)
                if prefix_edit == 'True':
                    message = '/me The prefix was set to: "{}"'.format(prefix)
                elif prefix_edit == 'None':
                    message = '/me Prefix possibilities: "{}"'.format(', '.join(prefix_possibles))
                elif prefix_edit == 'WrongSymbol':
                    message = '/me The prefix can not be modified to this symbol, type {}prefix to see the ' \
                              'possibilities.'.format(prefix)
                elif prefix_edit == 'Error':
                    message = '/me Incorrect Parameter.'
                message_temp = f"PRIVMSG #" + CHANNEL + " :" + message + "\r\n"
                s.send(message_temp.encode('utf-8'))
                print('{}: {}'.format(IDENTITY, message.encode('ascii', 'replace').decode()))
                return
        # elif message.lower().startswith(prefix+'owner'):

    old_commands_list = open("twitchbotDataFiles/commands_list.txt", 'r', encoding='utf-8')
    full_commands_list = list(map(str.strip, old_commands_list))
    commands = full_commands_list[0::4]
    old_commands_list.close()

    if message.startswith(prefix):
        sleep(10/100)
        if message[1:].lower() in commands:
            current_command = message[1:].lower()
            commands_position = (commands.index(current_command) + 1) * 4 - 3
            message = '' + full_commands_list[commands_position]
            if message.find('(__USER__)') != -1:
                message = message.replace('(__USER__)', user)
            if message.find('(__COUNT__)') != -1:
                command = current_command
                command_count_add()
                message = message.replace('(__COUNT__)', count_command)
            message_temp = f"PRIVMSG #" + CHANNEL + " :" + message + "\r\n"
            s.send(message_temp.encode('utf-8'))
            print('{}: {}'.format(IDENTITY, message.encode('ascii', 'replace').decode()))
            return

    old_autoreply_list = open("twitchbotDataFiles/autoreply_list.txt", 'r', encoding='utf-8')
    full_autoreply_list = list(map(str.strip, old_autoreply_list))
    autoreply_on_start = full_autoreply_list[0::3]
    autoreply_anywhere = ''.join([i for i in autoreply_on_start if "*" in i])
    autoreply_anywhere = autoreply_anywhere.strip('*').replace('*', ' ').split('  ')
    old_autoreply_list.close()

    if message.lower() in autoreply_on_start:
        sleep(10/100)
        current_reply = message.lower()
        autoreply_position = (autoreply_on_start.index(current_reply) + 1) * 3 - 2
        message = '' + full_autoreply_list[autoreply_position]
        if message.find('(__USER__)') != -1:
            message = message.replace('(__USER__)', user)
        if message.find('(__COUNT__)') != -1:
            autoreply = current_reply
            autoreply_count_add()
            message = message.replace('(__COUNT__)', count_reply)
        message_temp = f"PRIVMSG #" + CHANNEL + " :" + message + "\r\n"
        s.send(message_temp.encode('utf-8'))
        print('{}: {}'.format(IDENTITY, message.encode('ascii', 'replace').decode()))
        return

    if full_autoreply_list:
        if any(autoreply in message.lower() for autoreply in autoreply_anywhere):
            sleep(10/100)
            message = get_autoreply(message, autoreply_anywhere)
            if message == '':
                return
            elif message in autoreply_anywhere:
                current_reply = (' ' + message.lower() + ' ').replace(' ', '*')
                autoreply_position = (autoreply_on_start.index(current_reply) + 1) * 3 - 2
                message = '' + full_autoreply_list[autoreply_position]
                if message.find('(__USER__)') != -1:
                    message = message.replace('(__USER__)', user)
                if message.find('(__COUNT__)') != -1:
                    autoreply = current_reply
                    autoreply_count_add()
                    message = message.replace('(__COUNT__)', count_reply)
                message_temp = f"PRIVMSG #" + CHANNEL + " :" + message + "\r\n"
                s.send(message_temp.encode('utf-8'))
                print('{}: {}'.format(IDENTITY, message.encode('ascii', 'replace').decode()))
                return

    old_joke_list = open("twitchbotDataFiles/jokes_list.txt", 'r', encoding='utf-8')
    full_joke_list = list(map(str.strip, old_joke_list))
    old_joke_list.close()
    joke_caller = full_joke_list[0]

    if joke_caller in message.lower() and IDENTITY in message.lower():
        jokes = full_joke_list[1::2]
        joke = choice(jokes)
        message = '/me {}'.format(joke)
        message_temp = f"PRIVMSG #" + CHANNEL + " :" + message + "\r\n"
        s.send(message_temp.encode('utf-8'))
        print('{}: {}'.format(IDENTITY, message.encode('ascii', 'replace').decode()))
        sleep(10)
        joke_position = (full_joke_list.index(joke)) + 1
        message = '/me {} 😂😂😂'.format(full_joke_list[joke_position])
        message_temp = f"PRIVMSG #" + CHANNEL + " :" + message + "\r\n"
        s.send(message_temp.encode('utf-8'))
        print('{}: {}'.format(IDENTITY, message.encode('ascii', 'replace').decode()))
        return

    if message.startswith(prefix) and message.lower()[1:] in commands_exclusive:
        current_command = message[1:].lower()
        if current_command == 'command' or current_command == 'commands':
            message = '/me Commands list: {}'.format(", ".join(commands))
        elif current_command == 'autoreply' or current_command == 'autoreplies':
            message = '/me Autoreply list: {}'.format(", ".join(autoreply_on_start))
        else:
            return
        message_temp = f"PRIVMSG #" + CHANNEL + " :" + message + "\r\n"
        s.send(message_temp.encode('utf-8'))
        print('{}: {}'.format(IDENTITY, message.encode('ascii', 'replace').decode()))
        return
