#!/usr/bin/env python3
"""Module for network communication with serialization using sockets."""
import socket
import json

HOST = '127.0.0.1'
PORT = 65432


def start_server():
    """Start a server that receives and deserializes a dictionary."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(1)

        conn, addr = server.accept()
        with conn:
            data = b""
            while True:
                chunk = conn.recv(1024)
                if not chunk:
                    break
                data += chunk

            dictionary = json.loads(data.decode('utf-8'))
            print("Received Dictionary from Client:")
            print(dictionary)


def send_data(data):
    """Serialize and send a dictionary to the server.

    Args:
        data (dict): The dictionary to send.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((HOST, PORT))
            serialized = json.dumps(data).encode('utf-8')
            client.sendall(serialized)
    except Exception as e:
        print(f"Connection error: {e}")
