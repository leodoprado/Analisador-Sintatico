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
badcc - **Aceito** em 9 iterações <br/> 
dbcbdca - **Aceito** em 12 iterações <br/> 
babadbccc - **Aceito** em 15 iterações <br/> 
bababcdcbccc - **Aceito** em 20 iterações

**Sentenças Incorretas:** <br/>
dbcbdcd - **Erro** em 11 iterações <br/>
bababcdcaa - **Erro** em 16 iterações

# Getting started

### Install
```
$ pip3 install -r requirements.txt
```

### Run
```
$ python app.py
```
