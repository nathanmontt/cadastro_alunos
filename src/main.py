from pathlib import Path
import csv

caminho_csv = Path(__file__).parent.parent / "dados" / "brutos" / "alunos.csv"
with caminho_csv.open("r", encoding="utf-8-sig", newline="") as arq:
    leitor = csv.DictReader(arq, delimiter=";")
    for each_line in leitor:
        print(each_line)

    # for each_line in leitor:
    #     matricula = each_line["matricula"]
        # nome = each_line["nome"]
        # turma = each_line["turma"]
        # idade = each_line["idade"]
        # nota1 = each_line["nota1"]
        # nota2 = each_line["nota2"]
        # frequencia_pct = each_line["frequencia_pct"]

        # print(matricula)