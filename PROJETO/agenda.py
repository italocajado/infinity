from colorama import Fore, Back, Style

agenda = {}

def incluirCont (nome, tel):
    agenda[nome] = tel

def buscContatos():
    if len(agenda) == 0:
        print(Fore.RED + 'Agenda vazia')
        print(Style.RESET_ALL)
    else:
        print(agenda)  

def buscarContato(nome):
    if nome in agenda.keys():
        print(nome, " - ", agenda[nome])

def alterarContato(nome, tel):
    if nome in agenda:
        agenda[nome] = tel
        print(Fore.GREEN + '\nSUCESSO!')
        print(Style.RESET_ALL)


def excludeContato(nome):
    if nome in agenda:
        agenda.pop(nome)
    else:
        print(Fore.RED + "Contato não localizado !!")
        print(Style.RESET_ALL)

def limparAgenda():
    agenda.clear()

user = input('qual o seu nome: ')
while True:
    
    print(f'---------------------------- Agenda do {user} ------------------------------')
    opcao = int(input("Escolha uma opção: \n 1 - Adicionar contato; \n 2 - Alterar contato; \n 3 - Mostrar todos os contatos; \n 4 - Buscar contato; \n 5 - Excluir contato; \n 6 - Limpar agenda; \n 0 - Sair; \n")) 
    
    if opcao  == 1:
        nome = input('insira o nome do contato: ')
        tel = input('insira o tefone: ')
        incluirCont(nome, tel)
        print(Fore.GREEN + '\nSUCESSO!')
        print(Style.RESET_ALL)
    elif opcao == 2:
        nome = input('informe o nome: ')
        choice = int(input('Você deseja: \n 1 - Telefone; \n 2 - Nome\n'))
        if choice == 1:
            tel = input('insira o novo telefone: ')
            alterarContato(nome, tel)
    elif opcao == 3:
        buscContatos()
    elif opcao == 4:
        nome = input('digite o nome: ')
        buscarContato(nome)
    elif opcao == 5:
        nome = input('informe o nome para excluir: ')
        excludeContato(nome)
        print(agenda)
    elif opcao == 6:
        limparAgenda()
    elif opcao == 0:
        break
    else:
        print('Opção invalida')