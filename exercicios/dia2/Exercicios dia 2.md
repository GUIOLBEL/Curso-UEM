**Exercícios Capacitação Python \- Dia 2**

## **Aquecimento**

* **1\)** Leia um número inteiro fornecido pelo usuário via input(). Utilizando o operador de módulo (%), determine e imprima se ele é par ou ímpar usando if/else.

* **2\)** Leia dois números inteiros. Use um comparador simples (\>) e if/else para imprimir exclusivamente o valor do maior número. **Desafio extra:** determine o maior número sem utilizar if/else.

* **3\)** Leia uma palavra de qualquer tamanho. Usando o conceito de substrings (índices), acesse a primeira e a última letra. Verifique com if/else e imprima se ambas são iguais ou diferentes.

* **4\)** Leia um número inteiro. Verifique se o resto da divisão dele por 5 é igual a zero (% e \==). Imprima "É múltiplo" ou "Não é múltiplo".

* **5\)** Solicite uma senha ao usuário. Usando o comparador de igualdade (\==), verifique se a string digitada é exatamente "Admin123". Imprima "Liberado" ou "Bloqueado" usando if/else.

## **Avançando**

* **6\)** Leia um ano (ex: 2024). Um ano é bissexto se for divisível por 4, mas não pode ser divisível por 100, exceto se for divisível por 400\. Use operadores lógicos (and, or, not) e de módulo (%) em um único if para imprimir se é bissexto ou não.

* **7\)** Leia 3 valores inteiros representando os lados de um triângulo. Primeiro, verifique se eles podem formar um triângulo (a soma de dois lados quaisquer deve ser sempre maior que o terceiro). Se formar, use elif para classificar e imprimir: Equilátero (3 lados iguais), Isósceles (2 lados iguais) ou Escaleno (3 lados diferentes).

* **8\)** Leia 3 números inteiros distintos. Usando apenas comparadores (\>, \<) e operadores lógicos (and, or), descubra e imprima qual é o número mediano (aquele que não é o maior e nem o menor).

* **9\)** Uma loja dá descontos com base no valor da compra. Leia um valor float. Se a compra for menor que R$100, não há desconto. Se for entre R$100 e R$500, o desconto é de 10%. Acima de R$500, o desconto é de 20%. Use if/elif/else e operadores matemáticos (\*, \-) para calcular e imprimir o valor final.

* **10\)** Peça ao usuário para digitar três palavras distintas, uma de cada vez (em três inputs separados). Use o fatiamento de strings para pegar a primeira letra de cada palavra, concatene-as e verifique usando if/else se a sigla formada é "USP".

## **Desafios**

* **11\)** Leia 3 números inteiros aleatórios (variáveis a, b, c). Sem utilizar nenhuma função de ordenação pronta do Python (como sort ou max), crie a lógica usando apenas estruturas condicionais (if, elif, else) e operadores lógicos (and, or) para imprimir os três números em ordem crescente (do menor para o maior).

* **12\)** Peça um valor inteiro representando centavos (ex: 375 para R$ 3,75). Utilizando apenas a divisão inteira (//) e o módulo (%), calcule e imprima a quantidade exata e mínima de moedas de 100, 50, 25, 10, 5 e 1 centavo necessárias para compor esse valor. (Não use estruturas condicionais, apenas matemática sequencial).

* **13\)** Leia três inteiros representando dia, mês e ano. Usando condicionais if/elif/else e lógica (and, or), verifique se a data é válida. Lembre-se de que meses como abril têm 30 dias, fevereiro tem 28 (ou 29 em anos bissextos, aplicando a regra do exercício 6), e dias ou meses negativos/zerados não existem. Imprima "Data Válida" ou "Data Inválida".

* **14\)** Imagine duas linhas em uma régua. A linha 1 vai do ponto x1 ao x2. A linha 2 vai do ponto x3 ao x4. Leia esses 4 valores. Usando a lógica booleana e comparadores, determine e imprima usando if/else se as duas linhas se sobrepõem (se cruzam) em algum ponto ou se estão totalmente separadas.

* **15\)** Peça ao usuário para digitar uma palavra que tenha obrigatoriamente 5 letras. Não use métodos prontos de inversão. Apenas com acesso a posições específicas da string (ex: palavra\[0\], palavra\[4\]) e combinando múltiplos operadores and dentro de um if, verifique e imprima se a palavra é um palíndromo (lê-se igual de trás para frente, como "radar").

