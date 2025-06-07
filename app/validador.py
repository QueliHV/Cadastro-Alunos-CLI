def solicitar_nome():

    while True:
        nome = input("Informe o nome do aluno: \n")
        if nome:
            return nome
        
        print("Nome Inválido, tente novamente: ")


def solicita_nota(numero):
    while True:

        try:
            nota = float(input(f"Informe a nota {numero} \n"))

            if  0 <= nota <= 10:
                return nota
            else:
                print("A nota deve estar entre 0 e 10!")
        except ValueError as e:
            print(f"Erro: {e}. Certifique-se de digitar um número válido para a nota.")
