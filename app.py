from flask import Flask
import webview

app = Flask(__name__)
webview.create_window('Hello world', app)

if __name__ == "__main__":
    #app.run(debug=True)
    webview.start()
