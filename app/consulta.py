from app.util import limpa_tela, menu_retorno
from app.validador import solicitar_nome

def consultar_aluno(listaAlunos):

    limpa_tela()

    nome = solicitar_nome()

    # Busca pelo nome considerando sempre com letra minuscula
    alunoSelecionado = [aluno for aluno in listaAlunos if aluno['nome'].lower() == nome.lower()]
    
    if alunoSelecionado:
        for aluno in alunoSelecionado:
            print(f"Nome: {aluno['nome']}")
            print(f"Notas: {aluno['nota1']}, {aluno['nota2']}, {aluno['nota3']}")
            print(f"Média: {aluno['media']:.2f}\n")
    else:
        print("Aluno Não Cadastrado!")

    return menu_retorno()
        
