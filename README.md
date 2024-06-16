# TDE Compiladores - 2024 (pywebview)

### Analisador Sintático - Leonardo do Prado (T2021/1)

**Gramática:** <br/>
S ::= bAc | bC <br/>
A ::= dB | a <br/>
B ::= aC | bS | ε <br/>
C ::= b | cB

**First:** <br/>
S = { b } <br/>
A = { d, a } <br/>
B = { a, b, ε } <br/>
C = { b, c} 

**Follow:** <br/>
S = { $, a, b } <br/>
A = { b, c, a} <br/>
B = { $, a, b, c } <br/>
C = { a, b }

Tabela: <br/>
| - | A      | B      | C      | D      | $ 
| ------------- | :-------------: | :-------------: |  :-------------: |   :-------------: |   :-------------: |
| S | -      | - | - | -      | - |
| A | - | -      | -      | -      | - |
| B | - | -      | -   | -    | - |
| C | -      | - | -      | -      | - |

<br/>

Sentenças Corretas: <br/>
...

Sentenças Incorretas: <br/>
...

# Getting started

### Install
```
$ pip3 install -r requirements.txt
```

### Run
```
$ python app.py
```