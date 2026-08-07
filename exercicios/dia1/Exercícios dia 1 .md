**Exercícios Capacitação Python \- Dia 1**

**Aquecimento e Teoria**

1) Porque o Python é considerado uma linguagem interpretada? Quais são as vantagens e desvantagens de uma linguagem interpretada em comparação com as linguagens compiladas?

2) O que é um tipo de dado?

3) Quais são os tipos primitivos da linguagem Python e o que cada um busca representar?

4) Qual a ordem de precedência (sequência em que as operações são feitas) para as operações de tipo numérico (int e float)?

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

   * int(“24”)

   * float(14)

   * float(“8”)

   * float(“12,5”)

   * str(99)

   * int(“dez”)

7) O que são variáveis e como podemos declarar e inicializar uma em Python?

8) De o resultado de cada uma das interações abaixo. Utilize o IDLE para conferir suas respostas.

```py
>>> 10 + 4 / 2 * 5
?
>>> 10 + 4 / (2 * 5)
?
>>> (10 + 4) / 2 * 5
?
>>> 9 / 2
?
>>> 9 // 2
?
>>> 12 % 10 * 4
?
>>> 2 ** 2 * 2
?
>>> 2 ** (2 % 2)
?
>>> 16 ** (1 / 4)
?
>>> a: int = 10
>>> a + 5
?
>>> b: int = a - 8
>>> b * b
?
>>> a = 20
>>> b
?
>>> b = 6 / b
>>> b
?
>>> s: str = "Casa Amarela"
>>> s[1:7]
?
>>> s[:5]
?
>>> s[8:]
?
>>> s.lower()
?
>>> s[6:].upper()
?
>>> float(len(s))
?
>>> s + " Telhado Vermelho"
?
>>> int(9 * len('abaco')) % 10
?
>>> s[0] + s[3] + s[6] + s[9] + s[8] + s[1] * 3
```

**Praticando**

OBS: Antes de prosseguir, uma informação importante que vai ser muito útil nos próximos exercícios. A função print() não precisa receber necessariamente uma string para exibir, ela já faz a conversão sozinha para o tipo correto antes de exibir. Entretanto, se você quiser exibir algum valor de outro tipo junto de uma string, esse valor deve ser convertido para string e concatenado com a outra. A mesma coisa serve para a função input().

```py
print(10 + 1) # Exibe 11 na tela
print("O resultado da soma é " + str(2 + 2)) # Exibe: O resultado da soma é 4
```

9)  Faça um programa em Python que receba dois números do usuário e exiba o resultado da multiplicação desses dois números.

10)  Faça um programa que receba um número n e exiba o produto do antecessor de n com seu sucessor.

11)  Faça um programa que receba um número n e zere o valor da dezena e da unidade zerados (Ex: 1234 \-\> 1200, 100 \-\> 100, 42 \-\> 0). Dica: use a operação de piso da divisão ou módulo.

12)  Faça um programa que receba os valores de a, b e c de uma equação do segundo grau e calcule as raízes de x1 e x2 da equação pela Fórmula de Bhaskara.

13)  Faça um programa que receba uma string qualquer de entrada e exiba apenas a primeira metade dela com todas as letras em maiúsculo.

14)  Faça um programa que receba uma string e adicione n pontos de exclamação ao final dessa string. O valor de n é dado pelo usuário.

15)  No Brasil, usamos o padrão dia/mês/ano para representar datas. Já em alguns outros países, como nos Estados Unidos, o padrão usado é mês/dia/ano. Faça um programa que receba uma data no padrão brasileiro e retorne a data no padrão americano. Assuma que o mês e o dia sempre terão 2 dígitos, o ano 4 dígitos e sempre haverá um caractere de barra (/) separando eles.

16)  Uma prática muito comum em jogos online é a de criar nomes de usuário personalizados baseados no próprio nome. Faça um programa que receba o primeiro nome de uma pessoa e transforme ele em um nome de usuário com:

    * A letra do meio do nome em maiúscula (se o tamanho do nome for par, altere a letra a esquerda do meio)

    * O restante das letras devem estar em minúsculo

    * O nome deve iniciar com “Xx\_” e encerrar com “\_xX”

	Exemplos:

* Guilherme \-\>Xx\_guilHerme\_xX  
* Lucas \-\> Xx\_luCas\_xX  
* José \-\> Xx\_jOsé\_xX  
* NexTageBB \-\> Xx\_nextAgebb\_xX