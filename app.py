from flask import Flask, request, send_from_directory
import os
import socket

app = Flask(__name__, static_url_path='')

@app.route('/<path:path>')
def send_page(path):
    return send_from_directory('static', path)
@app.route('/')
def root():
    return app.send_static_file('index.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)
