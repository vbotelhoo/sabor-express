import os

restaurantes = [
    {'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
    {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
    {'nome':'Cantina', 'categoria':'Italiana', 'ativo':False}
]

def exibir_nome_programa():
    print("""

    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def listar_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listra Restaurantes')
    print('3. Alternar status do Restaurante')
    print('4. Sair\n')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def alternar_status_restaurante():
    exibir_subtitulos('Alternando o status do Restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulos('Listando todos os restaurante cadastrados:')

    print (f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20) } | {'Status'.ljust(20)}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        status_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {status_restaurante.ljust(20)}')

    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulos('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {
                            'nome':nome_do_restaurante,
                            'categoria':categoria,
                            'ativo':False
                            }

    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()

def exibir_subtitulos(texto):
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(f'{texto}')
    print(linha)

def opcao_invalida():
    print('Opcao invalida!\n')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('\nAperte a tecla ENTER para voltar ao menu principal ')
    main()

def finalizar_app():
    exibir_subtitulos('Encerrando a aplicação')

def main():
    os.system('clear')
    exibir_nome_programa()
    listar_opcoes()
    escolher_opcao()
    

if __name__ == '__main__':
    main()