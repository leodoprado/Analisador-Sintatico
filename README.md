# TDE Compiladores - 2024 (pywebview)

### Analisador Sintático - Leonardo do Prado (T2021/1)

**Gramática:** <br/>
S ::= bBa | cC <br/>
A ::= cCa | bS | ε <br/>
B ::= cCA | b <br/>
C ::= Bd | a

**First:** <br/>
S = { b, c } <br/>
A = { c, b, ε } <br/>
B = { c, b } <br/>
C = { c, b, a } 

**Follow:** <br/>
S = { $, a, d } <br/>
A = { a, d } <br/>
B = { a, d } <br/>
C = { a, b, c, d, $ }

Tabela: <br/>
| - | A      | B      | C      | D      | $ 
| ------------- | :-------------: | :-------------: |  :-------------: |   :-------------: |   :-------------: |
| S | -      | S ➔ bBa | S ➔ cC | -      | - |
| A | A ➔ ε | A ➔ bS  | A ➔ cCa| A ➔ ε | - |
| B | -      | B ➔ b   | B ➜ cCA| -      | - |
| C | C ➔ a | C ➔ Bd  | C ➔ Bd | -      | - |

<br/>

**Sentenças Corretas:** <br/> 
bcaa - **Aceito** em 9 iterações <br/>
bcbda - **Aceito** em 11 iterações <br/>
ccbdcaad - **Aceito** em 16 iterações <br/>
cccabbbadd - **Aceito** em 21 iterações

**Sentenças Incorretas:** <br/>
bbadcac - **Erro** em 6 iterações <br/>
cccababadd - **Erro** em 13 iterações

# Getting started

### Install
```
$ pip3 install -r requirements.txt
```

### Run
```
$ python app.py
```