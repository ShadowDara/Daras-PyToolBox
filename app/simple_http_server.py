import http.server
import socketserver

import socket

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("127.0.0.1", port)) == 0

def start_server(PORT, folder_path):
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"server path: {folder_path}\n")
        print(f"server runs on http://localhost:{PORT}\n")
        print("The Server runs forever now!\n")
        httpd.serve_forever()

def main(folder_path):
    PORT = 8000

    while PORT <= 49140:
        if is_port_in_use(PORT):
            print(f"Port {PORT} is busy, trying {PORT+1}")
            PORT += 1

        else:
            break

    if PORT > 49140:
        print("No usable Port found, Server could not start!")

    try:
        start_server(PORT, folder_path)

    except:
        print(f"Port {PORT} is busy")
