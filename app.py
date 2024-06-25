from flask import Flask, jsonify
from routes.home import home_route
import webview

app = Flask(__name__)

app.register_blueprint(home_route, url_prefix='/')  

webview.create_window('Analisador Sintático', app) 

if __name__ == "__main__":
    webview.start()
