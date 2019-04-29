import re

def le_terminal(expr):
	expr = remove_espacos(expr)
	print(expr)
	verifica_digit(expr)

def remove_espacos(texto) :
    remove = "\n\r "
    for i in range(0, len(remove)) :
        texto = texto.replace(remove[i],"")
    return texto

def verifica_digit(digit):
	# usando expressao regular para retirar os operadores e tranformando o resultado em string
	res = str("".join(map(str, re.findall(r"[\w]+", digit))))
	return res.isnumeric()

