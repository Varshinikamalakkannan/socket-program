import socket

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server is running...")

conn, addr = server.accept()
print("Connected to:", addr)

while True:
    data = conn.recv(1024).decode()

    if not data:
        break

    print("Client:", data)

    if data.lower() == "exit":
        conn.send("Connection closed.".encode())
        break

    reply = "Message received successfully."
    conn.send(reply.encode())

conn.close()
server.close()
