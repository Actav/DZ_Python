import socket
import threading

# Connection Data
host = '127.0.0.1'
port = 55555

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []

# Функция для широковещательной отправки сообщений клиентам
def broadcast(message, local_client):
    for client in clients:
        if client == local_client:
            continue
        client.send(message)

# Функция для удаления клиента из списка и закрытия соединения
def remove_client(client):
    index = clients.index(client)
    nickname = nicknames[index]

    broadcast('{} покинул чат!\n'.format(nickname).encode('utf-8'), client)

    nicknames.remove(nickname)
    clients.remove(client)
    client.close()

# Функция для обработки общения с клиентом
def handle_client_communication(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            broadcast(message.encode('utf-8'), client)
        except:
            remove_client(client)
            break

# Функция для проверки уникальности никнейма
def is_nickname_unique(nickname):
    return nickname not in nicknames

# Функция для обработки подключения нового клиента
def handle_new_client(client):
    client.send('NICK'.encode('utf-8'))
    nickname = client.recv(1024).decode('utf-8')

    while not is_nickname_unique(nickname):
        client.send('NICK_USED'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')

    nicknames.append(nickname)
    clients.append(client)
    print("Никнейм клиента: {}\n".format(nickname))

    broadcast("{} присоединился!".format(nickname).encode('utf-8'), client)
    client.send('Подключено к серверу!'.encode('utf-8'))

    threading.Thread(target=handle_client_communication, args=(client,)).start()

# Главный цикл сервера для ожидания новых подключений
def server_mainloop():
    print("Сервер в режиме ожидания...\n")
    while True:
        client, address = server.accept()
        print("Подключено к {}".format(str(address)))
        handle_new_client(client)

if __name__ == "__main__":
    try:
        server_mainloop()
    except KeyboardInterrupt:
        print("Сервер завершает работу...")
