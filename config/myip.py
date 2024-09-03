import socket


def getmyip():
    myip = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[1]
                         if not ip.startswith("127.")][:1],
                        [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(
                            socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
    return myip


if __name__ == "__main__":
    getmyip()
    print(getmyip())