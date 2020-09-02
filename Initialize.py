def join_room(s):
    read_buffer = ""
    loading = True

    while loading:
        read_buffer = read_buffer + s.recv(2048).decode('utf-8')
        temp = read_buffer.split("\n")
        read_buffer = temp.pop()

        for line in temp:
            loading = loading_complete(line)


def loading_complete(line):

    if "End of /NAMES list" in line:
        return False
    else:
        return True
