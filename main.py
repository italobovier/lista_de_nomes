# Lista de nomes
nomes = []

# Início do loop
while True:
    # Menu
    print('1 - Inserir novo nome')
    print('2 - Exibir lista de nomes')
    print('3 - Lista em ordem Alfabética')
    print('4 - Sair do Programa')

    opcao = input('Opção do usuário: ')

    # Verifica a opção escolhida
    match opcao:
        case '1':
            novo_nome = input("Insira o novo nome: ")
            nomes.append(novo_nome)
            print(f'{novo_nome} inserido com sucesso.')
            continue
        case '2':
            print('LISTA DE NOMES')
            if nomes:
                for nome in nomes:
                    print(f'\n{nome}\n')
            else:
                print('A lista está vazia.')
            continue
        case '3':
            nomes.sort()
            print('LISTA DE NOMES ORDENADA')
            for nome in nomes:
                print(f'\n{nome}\n')
            print('Lista ordenada com sucesso.')
            continue
        case '4':
            print('Encerrando o programa... ')
            break
        case _:
            print('Opção inválida. Por favor, escolha uma opção válida.')
