import conversorBib

try:
    input = raw_input   # compativel com python 2
except NameError:
    pass

def main():
	code = ''
	while (code != '/q'):
		code = input('> ')
		try:
			conversorBib.le_terminal(code)
		except Exception as e:
			print(e)

if __name__ == '__main__':
    main()