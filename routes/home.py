from flask import Blueprint, render_template, request, jsonify
from tokens.generate import gerar_sentenca

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    return render_template('index.html')

@home_route.route('/gerar_sentencas', methods=['POST'])
def gerar_sentencas():
    sentencesInput = gerar_sentenca()
    return render_template('index.html', sentencesInput=sentencesInput)

@home_route.route('/gerar_parsing', methods=['POST'])
def gerar_parsing():
    listsentencesInput = list(request.form.get('sentencesInput'))
    return render_template('index.html', listsentencesInput=listsentencesInput)
