from flask import Blueprint, render_template, request
from tokens import parser

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    return render_template('index.html')

@home_route.route('/', methods=['POST'])
def gerar_parsing():
    automaton = parser.Automaton()  # Cria uma instância do autômato para cada requisição
    listsentencesInput = request.form.get('sentencesInput')
    automaton.check_end(listsentencesInput)
    step_by_step = request.form.get('step_by_step') == 'true'
    return render_template('index.html', table=automaton.table, palavra=listsentencesInput, step_by_step=step_by_step)
