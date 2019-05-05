from ParserCalc import ParserCalc

try:
    input = raw_input
except NameError:
    pass

def main():
    while True:
        # ignorando espacos
        lst = list(input('> ').replace(' ', ''))
        if len(lst) == 0:
            print("Favor inserir uma expressao")
        else:
            ParserCalc(lst).parser(lst)

if __name__ == '__main__':
    main()