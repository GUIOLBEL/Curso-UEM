**Exercícios Capacitação Python \- Dia 1**

**Aquecimento e Teoria**

1) Porque o Python é considerado uma linguagem interpretada? Quais são as vantagens e desvantagens de uma linguagem interpretada em comparação com as linguagens compiladas?

Python é considerado uma linguagem interpretada porque ele “traduz” o código escrito em linguagem de máquina em tempo real durante a execução, sem passar por um processo de compilação. Isso permite um desenvolvimento mais acelerado, pois não é necessário esperar o código compilar, já que podemos modificar e testar diretamente. Entretanto, a sua velocidade de execução é mais lenta.

2) O que é um tipo de dado?

Tipos de dados são formas de representarmos informações no nosso programa, sejam números, caracteres, valores booleanos, entre outros tipos de informações.

3) Quais são os tipos primitivos da linguagem Python e o que cada um busca representar?

inteiro (int) \-\> números inteiros

números com ponto flutuante (float) \-\> representação aproximada dos números reais

strings (str) \-\>  cadeias de caracteres

booleano (bool) \-\> verdadeiro ou falso

4) Qual a ordem de precedência (sequência em que as operações são feitas) para as operações de tipo numérico (int e float)?

A ordem de precedência para operações com números é a mesma da matemática convencional: expressões entre parênteses \-\> exponenciação \-\> multiplicação e divisão \-\> adição e subtração.

5) Observe as cadeias de caracteres abaixo;

1. “Meu nome é Ronaldo”  
2. “flango\_Saulo2005’  
3. \*111.222.333-44\*  
4. ‘20 \+ 20 \+ 20 \+ 7’

	Quais  dessas cadeias representam corretamente uma string em linguagem Python?

1) I e III  
2) I e II  
3) I e IV  
4) II e III  
5) II e IV

6) Indique o resultado obtido por cada uma das operações de conversão de tipo.

   * int(“24”) 24

   * float(14) 14.0

   * float(“8”) 8.0

   * float(“12,5”) ERRO\! float não aceita vírgula (“,”) na conversão, deve ser usado um ponto (“.”) no lugar.

   * str(99) “99”

   * int(“dez”) ERRO\! Não é possível transformar letras em números.

7) O que são variáveis e como podemos declarar e inicializar uma em Python?

Variáveis são nomes que damos a espaços de memória onde podemos guardar dados de um determinado tipo. Em Python, podemos declarar uma variável com **nome: tipo** e inicializar ela com **nome \= valor**. Também podemos declarar e inicializar diretamente com **nome: tipo \= valor** ou omitir o tipo e deixar que o Python defina ele sozinho com **nome \= valor** diretamente sem declarar.

8) De o resultado de cada uma das interações abaixo. Utilize o IDLE para conferir suas respostas.

```py
>>> 10 + 4 / 2 * 5
20.0
>>> 10 + 4 / (2 * 5)
10.4
>>> (10 + 4) / 2 * 5
35.0
>>> 9 / 2
4.5
>>> 9 // 2
4
>>> 12 % 10 * 4
8
>>> 2 ** 2 * 2
8
>>> 2 ** (2 % 2)
1
>>> 16 ** (1 / 4)
2.0
>>> a: int = 10
>>> a + 5
15
>>> b: int = a - 8
>>> b * b
4
>>> a = 20
>>> b
2
>>> b = 6 / b
>>> b
3
>>> s: str = "Casa Amarela"
>>> s[1:7]
"asa Am"
>>> s[:5]
"Casa "
>>> s[8:]
"rela"
>>> s.lower()
"casa amarela"
>>> s[6:].upper()
"MARELA"
>>> float(len(s))
12.0
>>> s + " Telhado Vermelho"
"Casa Amarela Telhado Vermelho"
>>> int(9 * len('abaco')) % 10
5
>>> s[0] + s[3] + s[6] + s[9] + s[8] + s[1] * 3
"Cameraaa"
```

**Praticando**

OBS: Antes de prosseguir, uma informação importante que vai ser muito útil nos próximos exercícios. A função print() não precisa receber necessariamente uma string para exibir, ela já faz a conversão sozinha para o tipo correto antes de exibir. Entretanto, se você quiser exibir algum valor de outro tipo junto de uma string, esse valor deve ser convertido para string e concatenado com a outra. A mesma coisa serve para a função input().

```py
print(10 + 1) # Exibe 11 na tela
print("O resultado da soma é " + str(2 + 2)) # Exibe: O resultado da soma é 4
```

9)  Faça um programa em Python que receba dois números do usuário e exiba o resultado da multiplicação desses dois números.

```py
n1: int = int(input("Digite o primeiro número: "))
n2: int = int(input("Digite o segundo número: "))
print(str(n1) + " x " + str(n2) + " = " + str(n1 * n2))
```

10)  Faça um programa que receba um número n e exiba o produto do antecessor de n com seu sucessor.

```py
n: int = int(input("Digite um número: "))
print("O produto entre o sucessor e o antecessor de " + str(n) + " é " + str((n - 1) * (n + 1)))
```

11)  Faça um programa que receba um número n e zere o valor da dezena e da unidade zerados (Ex: 1234 \-\> 1200, 100 \-\> 100, 42 \-\> 0). Dica: use a operação de piso da divisão ou módulo.

```py
n: int = int(input("Digite um número: "))
# opção 1
zerado: int = (n // 100) * 100
# opção 2
zerado = n - (n % 100)
print("O número com a casa da dezena e da unidade zeradas é " + str(zerado))

```

12)  Faça um programa que receba os valores de a, b e c de uma equação do segundo grau e calcule as raízes de x1 e x2 da equação pela Fórmula de Bhaskara.

```py
print("CALCULADORA DE BASKARA")
a: int = int(input("Valor de a: "))
b: int = int(input("Valor de b: "))
c: int = int(input("Valor de c: "))

delta = b ** 2 - (4 * a * c)
x1 = (-b + delta ** (1 / 2)) / (2 * a)
x2 = (-b - delta ** (1 / 2)) / (2 * a)

print("As raizes da equação são:")
print("x1 = " + str(x1))
print("x2 = " + str(x2))
```

13)  Faça um programa que receba uma string qualquer de entrada e exiba apenas a primeira metade dela com todas as letras em maiúsculo.

```py
s: str = input("Digite qualquer texto: ")
metade: int = len(s) // 2 + 1
print(s[:metade].upper())

```

14)  Faça um programa que receba uma string e adicione n pontos de exclamação ao final dessa string. O valor de n é dado pelo usuário.

```py
s: str = input("Digite qualquer texto: ")
n: int = int(input(("Digite quantas exclamações quer adicionar: ")))
print(s + '!' * n)
```

15)  No Brasil, usamos o padrão dia/mês/ano para representar datas. Já em alguns outros países, como nos Estados Unidos, o padrão usado é mês/dia/ano. Faça um programa que receba uma data no padrão brasileiro e retorne a data no padrão americano. Assuma que o mês e o dia sempre terão 2 dígitos, o ano 4 dígitos e sempre haverá um caractere de barra (/) separando eles.

```py
data: str = input("Digite uma data no formato DD/MM/AAAA: ")
data_americano: str = data[3:5] + '/' + data[0:2] + data[5:]
print("A data no formato americano é: " + data_americano)
```

16)  Uma prática muito comum em jogos online é a de criar nomes de usuário personalizados baseados no próprio nome. Faça um programa que receba o primeiro nome de uma pessoa e transforme ele em um nome de usuário com:

    * A letra do meio do nome em maiúscula (se o tamanho do nome for par, altere a letra a esquerda do meio)

    * O restante das letras devem estar em minúsculo

    * O nome deve iniciar com “Xx\_” e encerrar com “\_xX”

	Exemplos:

* Guilherme \-\>Xx\_guilHerme\_xX  
* Lucas \-\> Xx\_luCas\_xX  
* José \-\> Xx\_joSé\_xX  
* NexTageBB \-\> Xx\_nextAgebb\_xX

```py
nome: str = input("Digite seu nome: ")
metade: int = len(nome) // 2
nome_usuario: str = nome[:metade].lower() + nome[metade].upper() + nome[metade + 1:].lower()
nome_usuario = "Xx_" + nome_usuario + "_xX"

print("Sua sugestão de nome de usuário é: " + nome_usuario)
```

