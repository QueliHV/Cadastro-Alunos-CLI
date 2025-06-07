from app.cadastro import cadastrar_aluno
from app.consulta import consultar_aluno
from app.listagem import listar_alunos
from app.util import limpa_tela

def mostrar_menu():

    todosAlunosCadastrados = []
    
    while(True):

        limpa_tela()

        print("======= CADASTRO DE ALUNOS =======")
        print("Escolha uma das opções abaixo:")

        escolha = input("1 - Cadastrar Aluno \n2 - Consultar Aluno \n3 - Listar Alunos \n4 - Sair \n")

        if (escolha == "4"):
            return False
        elif (escolha == "1"):
            todosAlunosCadastrados.append(cadastrar_aluno())
            
        elif (escolha == "2"):
            if consultar_aluno(todosAlunosCadastrados) == False:
                break
        elif (escolha == "3"):
            if listar_alunos(todosAlunosCadastrados) == False:
                break
        else:    
            print("Opção Invalida, escolha uma das opções abaixo:")    
        
