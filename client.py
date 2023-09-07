import socket
import threading

# Функция для ввода никнейма
def get_nickname():
    return input("Выберите ваш никнейм: ")

# Функция для получения сообщений от сервера
def receive_from_server(client_socket):
    global nickname

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == 'NICK':
                client_socket.send(nickname.encode('utf-8'))
            elif message == 'NICK_USED':
                while True:
                    print("Этот никнейм уже используется!")
                    new_nickname = get_nickname()
                    client_socket.send(new_nickname.encode('utf-8'))
                    if new_nickname != nickname:
                        nickname = new_nickname  # Обновляем глобальную переменную
                        break
            elif message == '/q':
                print("Соединение с сервером разорвано.")
                break
            else:
                print(message)
        except ConnectionAbortedError:
            print("Соединение с сервером разорвано.")
            break
        except:
            print("Произошла ошибка!")
            client_socket.close()
            break

# Функция для отправки сообщений на сервер
def send_to_server(client_socket):
    while True:
        message = input('')
        if message == '/q':
            client_socket.close()
            break

        client_socket.send('{}: {}'.format(nickname, message).encode('utf-8'))

if __name__ == "__main__":
    nickname = get_nickname()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 55555))

    receive_thread = threading.Thread(target=receive_from_server, args=(client_socket,))
    receive_thread.start()

    write_thread = threading.Thread(target=send_to_server, args=(client_socket,))
    write_thread.start()
