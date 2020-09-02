import socket
from Settings import HOST, PORT, PASS, IDENTITY, CHANNEL


def open_socket():
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(("PASS " + PASS + "\r\n").encode('utf-8'))
    s.send(("NICK " + IDENTITY + "\r\n").encode('utf-8'))
    s.send(("JOIN #" + CHANNEL + "\r\n").encode('utf-8'))
    return s


def send_message(s, message):
    message_temp = f"PRIVMSG #" + CHANNEL + " :" + message + "\r\n"
    s.send(message_temp.encode('utf-8'))
    print("Sent: " + message_temp)
