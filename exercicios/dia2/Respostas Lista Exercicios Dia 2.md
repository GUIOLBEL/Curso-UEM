**Gabarito e Explicações Lista de Exercícios Dia 2**

# **Aquecimento**

## **1\) Par ou Ímpar**

```py
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é Par.")
else:
    print("O número é Ímpar.")
```

**Explicação:** O operador de módulo (%) calcula o resto de uma divisão. Na matemática, qualquer número que dividido por 2 tenha resto igual a zero é par. Usamos a condicional if/else e o comparador de igualdade (==) para criar as duas rotas possíveis do programa.

## **2\) O Maior de Dois**

```py
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 > num2:
    print("O maior é:", num1)
elif num2 > num1:
    print("O maior é:", num2)
else:
    print("Os números são iguais.")
```

**Explicação:** Lemos os dois valores e usamos os comparadores lógicos de maior (\>). Adicionamos o elif para cobrir o cenário onde o segundo número é o maior, e o else garante o tratamento caso o usuário digite números iguais.

## **3\) Extremos da Palavra**

```py
palavra = input("Digite uma palavra: ")
tamanho = len(palavra)
# Acessa a primeira letra (índice 0) e a última (tamanho - 1)
primeira_letra = palavra[0]
ultima_letra = palavra[tamanho - 1]
if primeira_letra == ultima_letra:
    print("A primeira e a última letra são iguais.")
else:
    print("A primeira e a última letra são diferentes.")
```

**Explicação:** Utilizamos a função len() para descobrir o tamanho da string e o conceito de substrings (índices) para resgatar as letras. Como a contagem em programação começa no zero, a última letra sempre estará na posição tamanho \- 1\.

## **4\) Múltiplo de 5**

```py
numero = int(input("Digite um número: "))
if numero % 5 == 0:
    print("É múltiplo de 5.")
else:
    print("Não é múltiplo de 5.")
```

**Explicação:** Segue a mesma lógica do exercício 1\. O operador de módulo (%) verifica se há resto na divisão por 5\. Se o resto for 0, significa que a divisão é exata, ou seja, é um múltiplo.

## **5\) Acesso por Senha Simples**

```py
senha = input("Digite a senha: ")
if senha == "Admin123":
    print("Liberado")
else:
    print("Bloqueado")
```

**Explicação:** Avalia de forma direta a comparação entre a string digitada e a string esperada através do comparador de igualdade (==). O uso do if e else redireciona o usuário.

# **Avançando**

## **6\) Ano Bissexto**

```py
ano = int(input("Digite o ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é Bissexto.")
else:
    print("O ano NÃO é Bissexto.")
```

**Explicação:** Este é um ótimo teste para operadores lógicos combinados. O operador and garante que o ano é divisível por 4 E, ao mesmo tempo, não termina em 00 (não divisível por 100). O operador or cria uma exceção para essa regra: se for divisível por 400, é bissexto de qualquer forma.

## **7\) Validador de Triângulos**

```py
a = int(input("Lado 1: "))
b = int(input("Lado 2: "))
c = int(input("Lado 3: "))
# Verifica a condição de existência do triângulo
if (a + b > c) and (a + c > b) and (b + c > a):
    # Se existe, classifica
    if a == b and b == c:
        print("Triângulo Equilátero")
    elif a != b and a != c and b != c:
        print("Triângulo Escaleno")
    else:
        print("Triângulo Isósceles")
else:
    print("Os valores não podem formar um triângulo.")
```

**Explicação:** É feito um if principal validando a regra matemática básica da existência de triângulos através da união de condições com and. Dentro dele, usamos a estrutura if/elif/else para classificar o triângulo.

## **8\) O Número do Meio**

```py
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
if (a > b and a < c) or (a < b and a > c):
    print("O número mediano é:", a)
elif (b > a and b < c) or (b < a and b > c):
    print("O número mediano é:", b)
else:
    print("O número mediano é:", c)
```

**Explicação:** Para encontrar o meio sem ordenar a lista, isolamos cada variável. A variável a será a do meio se for maior que b e menor que c, OU se for menor que b e maior que c. Repetimos para b e, por exclusão, para c.

## **9\) Desconto Progressivo**

```py
valor = float(input("Digite o valor da compra: "))
if valor < 100:
    valor_final = valor
elif valor <= 500:
    valor_final = valor - (valor * 0.10) # 10% de desconto
else:
    valor_final = valor - (valor * 0.20) # 20% de desconto
print("O valor final a pagar é R$", valor_final)
```

**Explicação:** O código lê um float e usa a estrutura elif para impedir que condições se sobreponham. O cálculo do desconto utiliza operações de multiplicação (\*) e subtração (-).

## **10\) Gerador de Siglas**

```py
p1 = input("Palavra 1: ")
p2 = input("Palavra 2: ")
p3 = input("Palavra 3: ")
sigla = p1[0] + p2[0] + p3[0]
if sigla == "USP":
    print("A sigla formada é USP!")
else:
    print("A sigla formada é:", sigla)
```

**Explicação:** Pega a primeira letra de cada string e usa o operador de adição (+) para concatená-las. Em seguida, usa if/else para avaliar o resultado.

# **Desafios**

## **11\) Ordenação na Raça**

```py
a = int(input("Número 1: "))
b = int(input("Número 2: "))
c = int(input("Número 3: "))
if a <= b and a <= c:
    menor = a
    if b <= c:
        meio = b
        maior = c
    else:
        meio = c
        maior = b
elif b <= a and b <= c:
    menor = b
    if a <= c:
        meio = a
        maior = c
    else:
        meio = c
        maior = a
else:
    menor = c
    if a <= b:
        meio = a
        maior = b
    else:
        meio = b
        maior = a
print("Ordem crescente:", menor, meio, maior)
```

**Explicação:** Este exercício utiliza árvores de decisão lógica com if, elif e else. Primeiro definimos o menor absoluto e depois usamos um if interno para comparar os dois restantes.

## **12\) Troco Eficiente**

```py
centavos = int(input("Digite o valor em centavos: "))
m100 = centavos // 100
centavos %= 100
m50 = centavos // 50
centavos %= 50
m25 = centavos // 25
centavos %= 25
m10 = centavos // 10
centavos %= 10
m5 = centavos // 5
m1 = centavos % 5
print("Moedas de 100:", m100)
print("Moedas de 50:", m50)
print("Moedas de 25:", m25)
print("Moedas de 10:", m10)
print("Moedas de 5:", m5)
print("Moedas de 1:", m1)
```

**Explicação:** Testa a maestria das operações matemáticas. A divisão inteira (//) conta quantas moedas cabem, e o módulo (%) passa o resto para a próxima denominação.

## **13\) Validador de Data Completo**

```py
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))
data_valida = False
if dia > 0 and mes > 0 and ano > 0 and mes <= 12:
    if mes in [1, 3, 5, 7, 8, 10, 12] and dia <= 31:
        data_valida = True
    elif mes in [4, 6, 9, 11] and dia <= 30:
        data_valida = True
    elif mes == 2:
        bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
        if (bissexto and dia <= 29) or (not bissexto and dia <= 28):
            data_valida = True
if data_valida:
    print("Data Válida")
else:
    print("Data Inválida")
```

**Explicação:** Usamos uma variável booleana para checar todos os fluxos. O código valida o dia conforme o mês e as regras de ano bissexto.

## **14\) Interseção de Segmentos (1D)**

```py
x1 = int(input("Início da linha 1 (x1): "))
x2 = int(input("Fim da linha 1 (x2): "))
x3 = int(input("Início da linha 2 (x3): "))
x4 = int(input("Fim da linha 2 (x4): "))
if x2 < x3 or x1 > x4:
    print("As linhas não se sobrepõem.")
else:
    print("As linhas se sobrepõem.")
```

**Explicação:** É mais simples determinar quando as linhas não se tocam (uma termina antes da outra começar) do que mapear todos os tipos de sobreposição.

## **15\) Detetive de Palíndromos (Manual)**

```py
palavra = input("Digite uma palavra de 5 letras: ")
if len(palavra) != 5:
    print("Erro: A palavra deve ter exatamente 5 letras.")
else:
    if palavra[0] == palavra[4] and palavra[1] == palavra[3]:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")
```

**Explicação:** Comparamos os índices extremos (0 com 4, e 1 com 3\) para verificar a simetria da palavra, ignorando a letra central.  
