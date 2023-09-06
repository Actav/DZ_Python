import socket
import threading

# Начнем с глобальной переменной для хранения никнейма
nickname = ""

def get_nickname():
    return input("Выберите ваш никнейм: ")

def receive_from_server(client_socket):
    global nickname  # указываем, что мы используем глобальную переменную

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')

            if message == 'NICK':
                client_socket.send(nickname.encode('utf-8'))

            elif message == 'NICK_USED':
                print("Этот никнейм уже используется!")
                nickname = get_nickname()  # здесь мы обновляем глобальную переменную
                client_socket.send(nickname.encode('utf-8'))

            else:
                print(message)

        except ConnectionAbortedError:
            print("Соединение с сервером разорвано.")
            break

        except:
            print("Произошла ошибка!")
            client_socket.close()
            break

def send_to_server(client_socket):
    while True:
        message = input('')
        if message == '/q':
            client_socket.close()

            break

        client_socket.send('{}: {}'.format(nickname, message).encode('utf-8'))

if __name__ == "__main__":
    nickname = get_nickname()  # первоначальное присваивание никнейма

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 55555))

    receive_thread = threading.Thread(target=receive_from_server, args=(client_socket,))
    receive_thread.start()

    write_thread = threading.Thread(target=send_to_server, args=(client_socket,))
    write_thread.start()
