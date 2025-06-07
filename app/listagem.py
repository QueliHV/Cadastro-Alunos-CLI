
from app.util import limpa_tela
from app.util import menu_retorno

def listar_alunos(listaAlunos):

    limpa_tela()

    if(len(listaAlunos) == 0):
        print("Nenhum aluno Cadastrado!")
        return
    else:
        for aluno in listaAlunos:
            print(f"Nome: {aluno['nome']}")
            print(f"Notas: {aluno['nota1']}, {aluno['nota2']}, {aluno['nota3']}")
            print(f"Média: {aluno['media']:.2f}\n")

    return menu_retorno()        
            
