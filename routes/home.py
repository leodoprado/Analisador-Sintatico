from flask import Blueprint, render_template, request
from tokens.generate import gerar_sentenca
from tokens import parser

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
    automaton = parser.Automaton()  # Cria uma instância do autômato para cada requisição
    listsentencesInput = request.form.get('sentencesInput')
    
    # Verifica se o botão "Step by Step" foi clicado
    if 'step' in request.form:
        action = automaton.next_pass(listsentencesInput)
        return render_template('index.html', table=automaton.table, palavra=listsentencesInput, step_by_step=True, action=action)
    else:
        automaton.check_end(listsentencesInput)
        return render_template('index.html', table=automaton.table, palavra=listsentencesInput)
