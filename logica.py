import random

epsilon = "ε"
iteracao = 0
pile = "$S"
entry = ""
end = False
production = []
palavraInput = input("Insira a palavra de entrada: ")
table = []

class NonTerminal:
    def __init__(self, key, lista):
        self.key = key
        self.lista = lista

class Production:
    def __init__(self, nonTerminal, inicial, producao):
        self.nonTerminal = nonTerminal
        self.inicial = inicial
        self.producao = producao

def initSentence():
    global pile, entry, end
    sentence = "S"
    nTerminal = "S"

    while not all(x.islower() for x in sentence):
        for nonTerminal in production:
            if nonTerminal.key == nTerminal:
                prod = random.choice(nonTerminal.lista)
                if prod.producao != epsilon:
                    sentence = sentence.replace(nTerminal, prod.producao)
                else:
                    sentence = sentence.replace(nTerminal, '')

                match = next((x for x in sentence if x.isupper()), None)
                if match is None:
                    break
                nTerminal = match

    initAutomaton()

def initAutomaton():
    global table
    table = [(" ", "Pilha", "Entrada", "Ação")]

def initProduction(nTerminal, inicial, producao):
    exists = False
    for i, nonTerminal in enumerate(production):
        if nonTerminal.key == nTerminal:
            production.pop(i)
            exists = True
            break

    if not exists:
        nonTerminal = NonTerminal(nTerminal, [])
        production.append(nonTerminal)

    nonTerminal.lista.append(Production(nonTerminal, inicial, producao))
    return nonTerminal

def searchProduction(pile, char):
    for nonTerminal in production:
        if nonTerminal.key == pile:
            for prod in nonTerminal.lista:
                if prod.nonTerminal.key == pile and char in prod.inicial:
                    return prod
    return None

def nextPass():
    global pile, entry, iteracao, end
    if len(palavraInput) > 0:
        if end:
            initAutomaton()

        if not entry:
            entry = palavraInput + "$"

        action = ""
        charPile = pile[-1]
        pileTable = pile
        entryTable = entry
        pile = pile[:-1]
        iteracao += 1

        if charPile == entry[0] and charPile == "$":
            action = f"Aceito em {iteracao} iterações"
            end = True
        elif charPile and charPile.isupper():
            globalProductionMatch = searchProduction(charPile, entry[0])
            if globalProductionMatch:
                action = f"{globalProductionMatch.nonTerminal.key} -> {globalProductionMatch.producao}"
                if globalProductionMatch.producao != epsilon:
                    pile += globalProductionMatch.producao[::-1]
            else:
                end = True
                action = f"Erro em {iteracao} iterações!"
        elif charPile and charPile == entry[0]:
            action = f"Lê '{entry[0]}'"
            entry = entry[1:]
        else:
            end = True
            action = f"Erro em {iteracao} iterações!"

        insertRow(pileTable, entryTable, action)
        return action
    else:
        end = True

def checkEnd():
    global end
    action = ""
    initAutomaton()
    while not end:
        action = nextPass()
    print(action)

def insertRow(pile, entry, action):
    global table
    table.append((iteracao, pile, entry, action))

# Chamadas Iniciais
initAutomaton()

# S	→ bBa | S → cC	
production.append(initProduction("S", ["b"], "bBa"))
production.append(initProduction("S", ["c"], "cC"))

# A → ε | A → bS | A → cCa | A → ε
production.append(initProduction("A", ["a"], epsilon))
production.append(initProduction("A", ["b"], "bS"))
production.append(initProduction("A", ["c"], "cCa"))
production.append(initProduction("A", ["d"], epsilon))

# B	→ b | B → cCA
production.append(initProduction("B", ["b"], "b"))
production.append(initProduction("B", ["c"], "cCA"))

# C	→ a | C → Bd | C → Bd	
production.append(initProduction("C", ["a"], "a"))
production.append(initProduction("C", ["b"], "Bd"))
production.append(initProduction("C", ["c"], "Bd"))

checkEnd()

