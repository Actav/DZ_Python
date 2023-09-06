import socket
import threading

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(('127.0.0.1', 55555))
except ConnectionRefusedError:
    print("Сервер недоступен. Проверьте настройки сервера и попробуйте ещё раз.")
    exit()

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except ConnectionError:
            print("Сервер отключен.")
            client.close()
            break
        except OSError as e:
            print(f"Произошла ошибка: {e}")
        except Exception as e:
            print(f"Произошла неизвестная ошибка: {e}")

def write():
    while True:
        message = input('')
        if message.lower() == '/quit':
            client.send('/quit'.encode('utf-8'))
            client.close()
            break
        message = '{}: {}'.format(nickname, message)
        client.send(message.encode('utf-8'))

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
