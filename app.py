from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Obtém o nome do host da instância
    host_name = socket.gethostname()
    return f'Hello, World! This is instance {host_name}\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
