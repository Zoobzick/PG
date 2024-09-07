# import socket
#
#
# def getmyip():
#     myip = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[1]
#                          if not ip.startswith("127.")][:1],
#                         [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(
#                             socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
#     return myip
#
#
# if __name__ == "__main__":
#     getmyip()
#     print(getmyip())

import os
import socket

def get_dynamic_allowed_hosts():
    allowed_hosts = ['localhost', '127.0.0.1']


    try:
        # Получаем текущий IP-адрес сервера
        current_ip = socket.gethostbyname(socket.gethostname())
        allowed_hosts.append(f"{current_ip}:8000")
    except socket.error:
        pass  # Обработка ошибки при получении IP-адреса

    # Добавляем также IP-адрес, который может быть передан в переменной окружения
    additional_ip = os.getenv('ADDITIONAL_ALLOWED_IP')
    if additional_ip:
        allowed_hosts.append(additional_ip)

    return allowed_hosts
