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

    match operacao:
        case 1:
            item = input("Insira que item deseja adicionar: \n") 
            while item == "":
                print("Item não pode ser vazio! Insira um elemento válido!")
                item = input() 
            lista_compras.append(item)

        case 2:
            item = input("Insira que item deseja remover: \n")
            i = 0
            while i < len(lista_compras) and item != lista_compras[i]:
                i += 1
            if (not i == len(lista_compras)) and item == lista_compras[i]:
                lista_compras.pop(i)
                print("Item removido com sucesso!")
            else:
                print("O item inserido não consta na lista de compras")

        case 3:
            for item in lista_compras:
                print(item)

        case 0:
            executar = False

        case _:
            print("Insira um valor válido!")

print("Obrigado por usar meu programa!")
print("Até a próxima!!")