from ParserCalc import ParserCalc

try:
    input = raw_input
except NameError:
    pass

def main():
    while True:
        # ignorando espacos
        lst = list(input('> ').replace(' ', ''))
        ParserCalc(lst).parser(lst)

if __name__ == '__main__':
    main()