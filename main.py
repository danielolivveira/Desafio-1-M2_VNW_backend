# Missão 1: Restaurando as Regras Escolares 📝

# O vírus apagou os critérios de aprovação dos alunos! Para ajudar o Professor Byte a organizar o sistema, sua tarefa é criar um programa que verifique se um aluno foi aprovado (nota maior ou igual à 6) ou reprovado (nota menor ou igual à 5).

def verificar_aprovacao(nota):
    if nota >= 6:
        return "O aluno está aprovado"
    else:
        return "O aluno está reprovado"


nota_aluno = float(input("Digite a nota do aluno: "))
resultado = verificar_aprovacao(nota_aluno)
print(f"{resultado}.")


# Missão 2: O Sistema Eleitoral Secreto 📝

# O grêmio estudantil da escola realiza votações para decidir melhorias e inovações, mas o vírus desativou a verificação de elegibilidade para votar! Sua tarefa é criar um programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).

def verificar_elegibilidade(idade):
    if idade >= 16:
        return "Você pode votar"
    else:
        return "Você não pode votar"


idade_usuario = int(input("Digite sua idade: "))
resultado = verificar_elegibilidade(idade_usuario)
print(f"{resultado}.")


# Missão 3: Recuperando o Sistema de Notas 📊

# As classificações das provas desapareceram! Agora os alunos não sabem se tiraram um não sabem se tiraram um A, B, C, D ou F . Antes que o pânico se espalhe, sua tarefa é criar um programa que peça a nota do aluno e imprima sua classificação conforme a escala:

# - A (90-100) – "Parabéns, você tirou A!"
# - B (80-89) – "Muito bem, você tirou B."
# - C (70-79) – "Bom trabalho, você tirou C."
# - D (60-69) – "Fique atento, você tirou D."
# - F (menos de 60) – "Estude um pouco mais, você tirou F."

def verificar_classificacao(nota):
    if nota >= 90:
        return "Parabéns, você tirou A!"
    elif nota >= 80:
        return "Muito bem, você tirou B."
    elif nota >= 70:
        return "Bom trabalho, você tirou C."
    elif nota >= 60:
        return "Fique atento, você tirou D."
    else:
        return "Estude um pouco mais, você tirou F."


nota_aluno = float(input("Digite a nota do aluno: "))
resultado = verificar_classificacao(nota_aluno)
print(resultado)


# Missão 4: Restaurando a Identificação de Números ⚖️

# Os robôs da escola precisam identificar padrões numéricos para resolver cálculos e otimizar os sistemas. No entanto, o vírus bagunçou os algoritmos e agora eles não conseguem mais somar corretamente!

def somar_numeros(numero1, numero2):
    return numero1 + numero2


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
resultado = somar_numeros(numero1, numero2)
print(f"A soma dos números é {resultado:.2f}.")


# Missão 5: Recuperando o Cofre de Segurança 🔒

# O cofre da biblioteca guarda códigos raros de programação, mas o vírus resetou a senha! Agora, apenas quem souber a combinação correta poderá acessá-lo.
# Crie um programa que solicite ao usuário uma senha e verifique se ela está correta. A senha correta é "Python123".

def verificar_senha(senha):
    if senha == "Python123":
        return "Acesso liberado"
    else:
        return "Acesso negado"


senha_usuario = input("Digite a senha: ")
resultado = verificar_senha(senha_usuario)
print(resultado)


# Missão 6: Reforçando a Segurança e a Contagem do Sistema 💾

# O vírus está comprometendo o sistema de segurança e a contagem de registros! Para restaurar o funcionamento correto, você precisa reforçar as verificações e garantir que os dados sejam processados corretamente.
# Exiba os números de 1 a 10 usando um loop while.

numero = 1
while numero <= 10:
    print(numero)
    numero += 1


# Missão 7: Organizando a Lista📋

# Os números estão misturados e precisam ser organizados!
# Para resolver isso, você deve pegar os seguintes números: 8, 3, 10, 1 e 5, armazená-los em uma lista e depois exibi-los em ordem crescente. Isso ajudará a colocar tudo em ordem corretamente!

numeros = [8, 3, 10, 1, 5]
numeros.sort()
print(numeros)


# Missão 8: Acessando os Registros de Alunos 🏷️

# O sistema de alunos está desordenado! Para acessar as informações corretamente, você precisa organizar os dados.
# Crie uma tupla com os seguintes nomes: Ana, Bruno, Carla, Daniel, Eduardo e exiba o primeiro e o último nome.

alunos = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")
primeiro_nome = alunos[0]
ultimo_nome = alunos[-1]
print(primeiro_nome)
print(ultimo_nome)


# Missão 9: Calculando Dobro de um Número 🛠️

# Os alunos precisam de um programa que ajude em cálculos rápidos.
# Sua tarefa é criar uma função que receba um número e retorne o dobro do seu valor.
# ➡️ Exemplo: dobro(5)
# ➡️ Saída: "O dobro de 5 é 10"

def calcular_dobro(numero):
    return f"O dobro de {numero} é {numero * 2}"


numero = int(input("Digite um número: "))
resultado = calcular_dobro(numero)
print(resultado)


# Missão 10: Contando Letras 🔄

# O sistema precisa contar quantas letras há em um nome.
# ➡️ Crie uma função que receba um nome e diga quantas letras esse nome tem.
# ➡️ Exemplo: contar_letras("Ana")
# ➡️ Saída:" O nome Ana tem 3 letras"

def contar_letras(nome):
    return f"O nome {nome} tem {len(nome)} letras"


nome = input("Digite um nome: ")
resultado = contar_letras(nome)
print(resultado)
