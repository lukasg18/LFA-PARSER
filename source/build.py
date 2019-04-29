import parse_biblioteca

try:
    input = raw_input
except NameError:
    pass

def main():
	code = ''
	print("digite '/q' para sair do programa")
	while (code != '/q'):
		code = input('> ')
		try:
			parse_biblioteca.le_terminal(code)
		except Exception as e:
			print(e)

if __name__ == '__main__':
    main()