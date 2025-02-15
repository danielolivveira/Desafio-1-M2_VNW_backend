def verificar_aprovacao(nota):
    if nota >= 6:
        return "O aluno está aprovado"
    else:
        return "O aluno está reprovado"


nota_aluno = float(input("Digite a nota do aluno: "))
resultado = verificar_aprovacao(nota_aluno)
print(f"{resultado}.")
