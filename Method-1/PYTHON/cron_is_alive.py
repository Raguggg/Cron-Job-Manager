import socket

def start_server():
    host = '127.0.0.1'  # Localhost
    port = 8010  # Listening port

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f'Server listening on {host}:{port}')

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Accepted connection from {client_address}')

        data = client_socket.recv(1024).decode('utf-8')
        if 'GET /is-cron-live' in data:
            response = 'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nI am live'
        else:
            response = 'HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\n\r\n404 Not Found'

        client_socket.sendall(response.encode('utf-8'))
        client_socket.close()

if __name__ == '__main__':
    start_server()