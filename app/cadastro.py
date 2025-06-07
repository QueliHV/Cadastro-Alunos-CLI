
from app.util import limpa_tela
from app.validador import solicitar_nome, solicita_nota


def cadastrar_aluno():

    limpa_tela()
    nome = solicitar_nome()
    nota1 = solicita_nota(1)
    nota2 = solicita_nota(2)
    nota3 = solicita_nota(3)
    media = (nota1 + nota2 + nota3) / 3    

    aluno = {
        "nome": nome,
        "nota1" : nota1,
        "nota2" : nota2,
        "nota3" : nota3,
        "media" : media
    }
            
    return aluno
        
