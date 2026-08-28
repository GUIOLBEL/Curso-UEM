lista_compras: list[str] = []

print("Bem-Vindo à minha Lista de Compras!")

executar: bool = True
while executar: 
    print("Insira a operação que deseja realizar: ")
    print("1 -> Adicionar elemento na lista")
    print("2 -> Remover elemento da lista")
    print("3 -> Exibir toda a lista")
    print("0 -> Sair")
    operacao: int = int(input())
    item: str
    # Usando match-case
    match operacao:
        case 1:
            item = input("Insira que item deseja adicionar: \n") 
            # O \n adiciona uma quebra de linha, fazendo com que o usuário 
            # escreva na linha de baixo
            lista_compras.append(item)
            print("Item inserido com sucesso!")
        case 2:
            item = input("Insira que item deseja remover: \n")
            lista_compras.remove(item)
            print("Item removido com sucesso!")
        case 3:
            for item in lista_compras:
                print(item)
        case 0:
            executar = False
        case _:
            print("Insira um valor válido!")

    # # Usando if-else
    # if operacao == 1:
    #     item = input("Insira que item deseja adicionar: \n") 
    #     lista_compras.append(item)
    #     print("Item inserido com sucesso!")
    # elif operacao == 2:
    #     item = input("Insira que item deseja remover: \n")
    #     lista_compras.remove(item)
    #     print("Item removido com sucesso!")
    # elif operacao == 3:
    #     for i in lista_compras:
    #         print(i)
    # elif operacao == 0:
    #     executar = False
    # else: 
    #     print("Insira um valor válido!")

print("Obrigado por usar meu programa!")
print("Até a próxima!!")