import os

def limpa_tela():
    os.system('clear')


def menu_retorno():
    while True:

        escolha = input("1 - Voltar ao menu inicial \n2 - Encerrar programa\n")
        if escolha == "1":
            return True
        elif escolha == "2":
            return False
        else:
            print("Opção Inválida!")
