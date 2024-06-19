# TDE Compiladores - 2024 (pywebview)

### Analisador Sintático - Leonardo do Prado (T2021/1)

**Gramática:** <br/>
S ::= bBc | dCa <br/>
A ::= aCb | cBd <br/>
B ::= aCc | b | ε <br/>
C ::= bAc | d

**First:** <br/>
S = { b, d } <br/>
A = { a, c } <br/>
B = { a, b, ε } <br/>
C = { b, d } 

**Follow:** <br/>
S = { $ } <br/>
A = { c } <br/>
B = { c, d } <br/>
C = { a, b, c }

Tabela: <br/>
| - | A      | B      | C      | D      | $ 
| ------------- | :-------------: | :-------------: |  :-------------: |   :-------------: |   :-------------: |
| S | - | S → bBc | - | S → dCa | - |
| A | A → aCb | -  | A → cBd | - | - |
| B | B → aCc | B → b | B → ε | B → ε | - |
| C | - | C → bAc | C → d | -      | - |

<br/>

**Sentenças Corretas:** <br/> 


**Sentenças Incorretas:** <br/>


# Getting started

### Install
```
$ pip3 install -r requirements.txt
```

### Run
```
$ python app.py
```
