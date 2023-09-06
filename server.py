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

# Sending Messages To All Connected Clients
def broadcast(message, sender=None):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                # Remove and close broken connections
                remove_client(client)

# Removing a Client
def remove_client(client):
    index = clients.index(client)
    nickname = nicknames[index]
    clients.remove(client)
    nicknames.remove(nickname)
    client.close()
    broadcast(f"{nickname} left the chat.".encode('utf-8'))

# Handling Messages From Clients
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                remove_client(client)
                break
            broadcast(message, client)
        except:
            remove_client(client)
            break

# Receiving / Listening Function
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # Request And Store Nickname
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')

        if nickname in nicknames:
            client.send("Nickname already in use. Please choose another one.".encode('utf-8'))
            client.close()
            continue

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname is {nickname}")
        broadcast(f"{nickname} joined the chat.".encode('utf-8'))
        client.send("Connected to the chat server.".encode('utf-8'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

if __name__ == "__main__":
    print("Server is listening...")
    receive()
