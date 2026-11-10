from pathlib import Path
import csv

caminho_csv = Path(__file__).parent.parent / "dados" / "brutos" / "alunos.csv"

with caminho_csv.open("r", encoding="utf-8-sig", newline="") as arq:
    leitor = csv.DictReader(arq, delimiter=";")
    # for each_line in leitor:
    #     print(each_line)
    count_A = 0
    count_B = 0
    count_C = 0

    for each_line in leitor:
        matricula = each_line["matricula"]
        nome = each_line["nome"].strip().title()
        turma = each_line["turma"]
        
        idade = each_line["idade"]
        if idade:
            idade = int(idade)
        else:
            idade = None

        # idade = each_line["idade"]
        nota1 = each_line["nota1"]
        nota2 = each_line["nota2"]
        frequencia_pct = each_line["frequencia_pct"]

        # idade_texto = each_line["idade"].strip()

        # if idade_texto:
        #     idade = int(idade_texto)
        # else:
        #     idade = None

        # qual turma é a mais predominante?
        if turma == 'A':
            count_A += 1
        elif turma == 'B':
            count_B += 1
        elif turma == 'C':
            count_C += 1

        print(matricula, nome, turma, idade)

    print(count_A)
    print(count_B)
    print(count_C)