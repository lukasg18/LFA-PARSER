# LFA-Parser
Implementação de um parser descendente recursivo para uma Linguagem Livre de Contexto, chamada de MEL.

### Informações gerais
- **Autor**: Lucas Gomes Flegler
- **Linguagem de programação**: Python (versão 3.6.5)
- **Ambiente de desenvolvimento**: Visual Studio Code (versão 1.33.1)

### Descrição geral do código fonte
O código fonte está estruturado da seguinte maneira:

* src
  - main.py
  - mel.py
  - trab1.sh
  - testes




##### mel.py
É um módulo que contém uma classe única chamada `MEL`, que tem por responsabilidade manipular as expressões matemáticas e encontrar o seu resultado.

```python
class MEL():
    def __init__(self, tokens):
        self._tokens = tokens
        self._current = tokens[0]
        self._operator = ''
    
    def mount_expression(self, lst):
        tokens = []
        numbers, operators = '', ''

        for i in range(len(lst)):
            # concatenando numeros seguidos por numeros, numeros com '.' e numeros com 'e'
            if (self.digit(lst[i]) or lst[i] == '.' or lst[i] == 'e' or lst[i] == 'E'):
                numbers += lst[i]
                if operators != '':
                    tokens.append(operators)
                    operators = ''
            else:
                # se ja existe um operador '/'
                if operators != '':
                    # caso a expressao tenha '//', ambos ficam na mesma posicao da lista
                    if (operators is '/' and lst[i] is '/'):
                        operators += lst[i]
                    else:
                        tokens.append(operators)
                        tokens.append(lst[i])
                        operators = ''
                else:
                    operators += lst[i]
                if numbers != '':
                    tokens.append(numbers)
                    numbers = ''

        # caso só exista somente numeros como entrada
        if (numbers != '' and operators == ''):
            tokens.append(numbers)
        return tokens
    
    def parser(self,lst):
        tokens = []
        # caso a expressao nao seja aceita
        try:
            tokens = self.mount_expression(lst)
            print(MEL(tokens).exp())
        except:
            print("expressao invalida")

```
O trecho de codigo mostrado acima representa o construtor da classe. O construtor contém o "token", que é responsavel por amazenar a expressao inserida, o "current" que armazena a posição atual da expressao a ser processada e o operador que verifica se a expressao é negativa ou positiva.

O mesmo trecho citado acima também mostra o método chamado `parser`, que tem por responsabilidade ser um intermediario entre a montagem da expressao e a chamada da mesma.
O método `parser` depois de executado, chamará os demais metodos da classe, seguindo as regras de produção definidas para a gramática que é mostrada logo abaixo.

* expr ::= term (('+' | '-') term)*
* term ::= factor (('*' | '/' | '//' | '%') factor)*
* factor ::= base ('^' factor)?
* base ::= (-) base | '(' expr ')'
* digit ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'


##### main.py
É o módulo que é contruido e que contém a execução principal do programa, o qual utiliza o módulo `ParserMEL.py` que contém a classe do parser e instancia um objeto fazendo chamada o método `parseExpression` passando como argumento a expressão e recebendo um valor como resultado. Como se pode notar no trecho abaixo a expressão é digitada pelo usuário.

```python
from mel import MEL

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
            MEL(lst).parser(lst)

if __name__ == '__main__':
    main()
```

### Como executar?
Para buildar/executar o app no ambiente Linux basta abrir o CLI(Command Line Interface) no diretório __/source__ e digitar o seguinte comando:
    
    python3 build.py

Neste comando como o SO é o Linux dist. Ubuntu 18.04 e já contém as versões ***2.7.15 e 3.6.7*** como default, o que torna fácil a execução de código utilizando esta linguagem. O outro comando seria a execução do arquivo .sh criado no mesmo diretório. Abaixo execute o mesmo comando que produzirá a mesma ação do primeiro comando mostrado acima:

    sh trab1.sh
    
### Informações adicionais
Todo o código fonte está hospedado no meu [GitHub](https://github.com/lukasg18/LFA-PARSER).

