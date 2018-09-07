from flask import Flask, request, send_from_directory
import os
import socket

app = Flask(__name__, static_url_path='')

@app.route("/")
def hello():
    html = "<h3>Hello, GoPomelo !</h3>"
    return html
@app.route('./mdl/')
def send_js(path):
    return send_from_directory('mdl', path)
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)
