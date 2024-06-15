import random

def gerar_sentenca():
    sentencas = [
        'cbaaababd',
        'badc',
        'cbaabadccdca',
        'babadccc',
        'cbaca',
        'babaabaccdccc'
    ]
    sentenca_aleatoria = random.choice(sentencas)
    print(sentenca_aleatoria)

gerar_sentenca()