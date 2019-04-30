import re
from operator import add, sub, mul, truediv, floordiv

def parser_desc(expr):
	expr = remove_espacos(expr)
	# print(re.findall(r"([0-9]*[+-/%\*]*)",expr))
	print(verifica_digit(expr))

def remove_espacos(texto) :
    remove = "\n\r "
    for i in range(0, len(remove)) :
        texto = texto.replace(remove[i],"")
    return texto

def verifica_digit(char):
	digits = ['0','1','2','3','4','5','6','7','8','9']
	if char in digits:
		return True
	else:
		return False

