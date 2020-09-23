n = 1
alunosrec = 1

while n != 0:
    nota = float(input("Digite a nota do aluno: "))
    if nota >= 3 and nota < 5:
        alunosrec
    else:
        alunosrec = alunosrec - 1

    print("Alunos em recuperação: ", alunosrec)
    alunosrec = alunosrec + 1
    n = n + 1
