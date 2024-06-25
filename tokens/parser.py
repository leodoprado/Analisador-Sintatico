epsilon = "ε"

class Automaton:
    def __init__(self):
        self.iteracao = 0
        self.stack = "$S"
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


    def search_production(self, stack, char):
        for nonTerminal in self.production:
            if nonTerminal.key == stack:
                for prod in nonTerminal.lista:
                    if char in prod.inicial:
                        return prod
        return None

    def next_stage(self, sentenceInput):
        if not sentenceInput:
            self.end = True
            return

        if self.end:
            self.init_automaton()

        if not self.entry:
            self.entry = sentenceInput + "$"

        action = ""
        charStack = self.stack[-1]
        stackTable = self.stack
        entryTable = self.entry
        self.stack = self.stack[:-1]
        self.iteracao += 1

        if charStack == self.entry[0] and charStack == "$":
            action = f"Aceito em {self.iteracao} iterações"
            self.end = True
        elif charStack.isupper():
            globalProductionMatch = self.search_production(charStack, self.entry[0])
            if globalProductionMatch:
                action = f"{globalProductionMatch.nonTerminalKey} -> {globalProductionMatch.producao}"
                if globalProductionMatch.producao != epsilon:
                    self.stack += globalProductionMatch.producao[::-1]
            else:
                self.end = True
                action = f"Erro em {self.iteracao} iterações!"
        elif charStack == self.entry[0]:
            action = f"Lê '{self.entry[0]}'"
            self.entry = self.entry[1:]
        else:
            self.end = True
            action = f"Erro em {self.iteracao} iterações!"

        self.insert_row(stackTable, entryTable, action)
        return action

    def check_end(self, sentenceInput):
        self.init_automaton()
        while not self.end:
            action = self.next_stage(sentenceInput)
        return action

    def insert_row(self, stack, entry, action):
        self.table.append((self.iteracao, stack, entry, action))

    def initialize(self):
        self.iteracao = 0
        self.stack = "$S"
        self.entry = ""
        self.end = False
        self.production = []
        self.table = []

        self.init_automaton()

        # S → b | S → d
        self.init_production("S", ["b"], "bBc")
        self.init_production("S", ["d"], "dCa")

        # A → a | A → c
        self.init_production("A", ["a"], "aCb")
        self.init_production("A", ["c"], "cBd")

        # B → a | B → b | B → ε | B → ε
        self.init_production("B", ["a"], "aCc")
        self.init_production("B", ["b"], "b")
        self.init_production("B", ["c"], epsilon)
        self.init_production("B", ["d"], epsilon)

        # C → b | C → c
        self.init_production("C", ["b"], "bAc")
        self.init_production("C", ["d"], "d")

class Production:
    def __init__(self, nonTerminalKey, inicial, producao):
        self.nonTerminalKey = nonTerminalKey
        self.inicial = inicial
        self.producao = producao

class NonTerminal:
    def __init__(self, key, lista):
        self.key = key
        self.lista = lista