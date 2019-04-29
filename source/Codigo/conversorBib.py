def le_terminal(expr):
	expr = remove_caracter(expr)
	print(expr)

def remove_caracter(texto) :
    remove = "\n\r\s "
    for i in range(0, len(remove)) :
        texto = texto.replace(remove[i],"")
    return texto

def quebra_lista(lista, n):
	return [lista[i:i+n] for i in range(0, len(lista), n)]

def lista_para_caracter(lista):
	texto = ''
	for index in lista:
		texto += ' ' + index
	return texto

def separa_informacoes(matriz_generica, nome_saida):
	dicionario = {}
	trans = []
	out_fn = []
	enum = 0

	for pos_matriz in matriz_generica:

		if 'mealy' in pos_matriz or 'moore' in pos_matriz:
			dicionario['nome'] = pos_matriz[0]

		elif 'symbols-in' in pos_matriz:
			dicionario['symbols-in'] = pos_matriz[1:]

		elif 'symbols-out' in pos_matriz:
			dicionario['symbols-out'] = pos_matriz[1:]

		elif 'states' in pos_matriz:
			dicionario['states'] = pos_matriz[1:]

		elif 'finals' in pos_matriz:
			dicionario['finals'] = pos_matriz[1:]

		elif 'start' in pos_matriz:
			dicionario['start'] = pos_matriz[1:]

		elif 'trans' in pos_matriz:
			enum = 1

		elif 'out-fn' in pos_matriz:
			enum = 2
			
		elif enum == 1:
			trans.extend(pos_matriz)
			dicionario['trans'] = trans

		elif enum == 2:
			out_fn.extend(pos_matriz)
			dicionario['out-fn'] = out_fn

	if dicionario['nome'] == 'mealy':
		dicionario['trans'] = quebra_lista(dicionario['trans'], 4)
	else :
		dicionario['trans'] = quebra_lista(dicionario['trans'], 3)
		dicionario['out-fn'] = quebra_lista(dicionario['out-fn'], 2)
	return 0
