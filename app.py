from flask import Flask, jsonify
from routes.home import home_route
import webview

app = Flask(__name__)

#webview.create_window('Analisador Sintático', app)

app.register_blueprint(home_route, url_prefix='/')   

if __name__ == "__main__":
    app.run(debug=True)
    #webview.start()
