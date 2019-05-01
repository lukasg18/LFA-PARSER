"""
expr ::= term ((‘+’ | ‘-’) term)*
term ::= factor ((‘*’ | ‘/’ | ‘//’ | ‘%’) factor)*
factor ::= base (‘^’ factor)?
base ::= (‘+’ | ‘-’) base | number | ‘(’ expr ‘)’
number ::= digit+ ‘.’? digit* ((‘E’ | ‘e’) (‘+’ | ‘-’)? digit+)?
digit ::= ‘0’ | ‘1’ | ‘2’ | ‘3’ | ‘4’ | ‘5’ | ‘6’ | ‘7’ | ‘8’ | ‘9’
"""

class ParserCalc():
    def __init__(self, tokens):
        self._tokens = tokens
        self._current = tokens[0]
    
    def parser(self,lst):
        tokens = []
        for i in range(len(lst)):
            if lst[i].isdigit() and i > 0 and  (tokens[-1].isdigit() or tokens[-1][-1] is '.'):
                # se ele encontrar 2 ou mais numeros em seguida ou um numero com '.', ele concatena  para uma unica posicao da lista       
                tokens[-1] += lst[i] 
            elif lst[i] is '.' and i > 0 and tokens[-1].isdigit():
                tokens[-1] += lst[i]
            else:
                tokens.append(lst[i])
        print(ParserCalc(tokens).exp())

    def exp(self):
        result = self.term()
        while self._current in ('+', '-'):
            if self._current == '+':
                self.next()
                result += self.term()
            if self._current == '-':
                self.next()
                result -= self.term()
        return result

    def term(self):
        result = self.factor()
        while self._current in ('*', '/'):
            if self._current == '*':
                self.next()
                result *= self.term()
            if self._current == '/':
                self.next()
                result /= self.term()
        return result

    def factor(self):
        result = None
        if self._current[0].isdigit() or self._current[-1].isdigit():
            result = float(self._current)
            self.next()
        elif self._current is '(':
            self.next()
            result = self.exp()
            self.next()
        return result

    def next(self): 
        #pula o primeiro elemento, pois ele ja foi processado
        self._tokens = self._tokens[1:] 
        if len(self._tokens) > 0:
            # coloca o proximo elemento a ser processado
            self._current = self._tokens[0]
