import random

epsilon = "ε"

class Automaton:
    def __init__(self):
        self.iteracao = 0
        self.pile = "$S"
        self.entry = ""
        self.end = False
        self.production = []
        self.table = []
        self.initialize()

    def init_automaton(self):
        self.table = []

    def init_production(self, nTerminal, inicial, producao):
        for nonTerminal in self.production:
            if nonTerminal.key == nTerminal:
                nonTerminal.lista.append(Production(nTerminal, inicial, producao))
                return nonTerminal
            
        nonTerminal = NonTerminal(nTerminal, [Production(nTerminal, inicial, producao)])
        self.production.append(nonTerminal)
        return nonTerminal


    def search_production(self, pile, char):
        for nonTerminal in self.production:
            if nonTerminal.key == pile:
                for prod in nonTerminal.lista:
                    if char in prod.inicial:
                        return prod
        return None

    def next_pass(self, palavraInput):
        if not palavraInput:
            self.end = True
            return

        if self.end:
            self.init_automaton()

        if not self.entry:
            self.entry = palavraInput + "$"

        action = ""
        charPile = self.pile[-1]
        pileTable = self.pile
        entryTable = self.entry
        self.pile = self.pile[:-1]
        self.iteracao += 1

        if charPile == self.entry[0] and charPile == "$":
            action = f"Aceito em {self.iteracao} iterações"
            self.end = True
        elif charPile.isupper():
            globalProductionMatch = self.search_production(charPile, self.entry[0])
            if globalProductionMatch:
                action = f"{globalProductionMatch.nonTerminalKey} -> {globalProductionMatch.producao}"
                if globalProductionMatch.producao != epsilon:
                    self.pile += globalProductionMatch.producao[::-1]
            else:
                self.end = True
                action = f"Erro em {self.iteracao} iterações!"
        elif charPile == self.entry[0]:
            action = f"Lê '{self.entry[0]}'"
            self.entry = self.entry[1:]
        else:
            self.end = True
            action = f"Erro em {self.iteracao} iterações!"

        self.insert_row(pileTable, entryTable, action)
        return action

    def check_end(self, palavraInput):
        self.init_automaton()
        while not self.end:
            action = self.next_pass(palavraInput)
        return action

    def insert_row(self, pile, entry, action):
        self.table.append((self.iteracao, pile, entry, action))

    def initialize(self):
        self.iteracao = 0
        self.pile = "$S"
        self.entry = ""
        self.end = False
        self.production = []
        self.table = []

        self.init_automaton()

        self.init_production("S", ["b"], "bBa")
        self.init_production("S", ["c"], "cC")

        self.init_production("A", ["a"], epsilon)
        self.init_production("A", ["b"], "bS")
        self.init_production("A", ["c"], "cCa")
        self.init_production("A", ["d"], epsilon)

        self.init_production("B", ["b"], "b")
        self.init_production("B", ["c"], "cCA")

        self.init_production("C", ["a"], "a")
        self.init_production("C", ["b"], "Bd")
        self.init_production("C", ["c"], "Bd")

class Production:
    def __init__(self, nonTerminalKey, inicial, producao):
        self.nonTerminalKey = nonTerminalKey
        self.inicial = inicial
        self.producao = producao

class NonTerminal:
    def __init__(self, key, lista):
        self.key = key
        self.lista = lista