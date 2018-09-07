from flask import Flask, request
import os
import socket

app = Flask(__name__, static_url_path='')

@app.route("/")
def hello():
    html = "<h3>Hello, GoPomelo !</h3>"
    return html
@app.route('/mdl/')
def root():
    return app.static_folder('static')

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)
