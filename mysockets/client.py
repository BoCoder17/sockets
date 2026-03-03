import socket

# Адрес и порт сервера, к которому будет выполняться подключение
server_host = '127.0.0.1' # Специальный IP-адрес loopback
server_port = 8888 # Порт

# Создаем сокет, протоколы IP и TCP
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

s.connect((server_host, server_port)) # Подключаемся к серверу
s.sendall(b'Hello World from BoCoder!') # Отправляем данные на сервер

data = s.recv(1024) # Получаем данные от сервера

s.close() # Закрываем сокет

print('Полученные данные:', data) # Печатаем данные, которые получили от сервера