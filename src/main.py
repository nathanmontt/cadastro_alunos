from pathlib import Path
import csv

caminho_csv = Path(__file__).parent.parent / "dados" / "brutos" / "alunos.csv"

with caminho_csv.open("r", encoding="utf-8-sig", newline="") as arq:
    leitor = csv.DictReader(arq, delimiter=";")
    count_A = 0
    count_B = 0
    count_C = 0

    for each_line in leitor:
        matricula = each_line["matricula"]

        # verifcação de nomes
        nome_old = each_line["nome"].strip().title()
        if not nome_old:
            nome = "Sem registro"
        else:
            nome = nome_old

        # ---------------------------------------

        turma = each_line["turma"]

        # ---------------------------------------
        # verificação de idades
        idade_texto = each_line["idade"].strip()
        idade_extenso = {
            "dezesseis": 16,
        }
        if idade_texto.isdigit():
            idade = int(idade_texto)
        elif idade_texto.casefold() in idade_extenso:
            idade = idade_extenso[idade_texto]
        else:
            idade = "Sem idade"

        # ---------------------------------------
        # verificação de nota
        nota1_texto = each_line["nota1"].strip().casefold()
        nota2_texto = each_line["nota2"].strip().casefold()
        if nota1_texto == "ausente" or nota2_texto == "ausente":
            nota1_texto = 0
            nota2_texto = 0

        if not nota1_texto or not nota2_texto:
            nota1 = None
            nota2 = None
        else:
            nota1 = float(nota1_texto.replace(',','.'))
            nota2 = float(nota2_texto.replace(',','.'))


        # ---------------------------------------
        # verificação de frequencia
        frequencia_pct = each_line["frequencia_pct"]

        # ---------------------------------------
        # verificação de turma predominante
        if turma == 'A':
            count_A += 1
        elif turma == 'B':
            count_B += 1
        elif turma == 'C':
            count_C += 1

        # print dos valores
        print(f"{matricula} | {nome} | {turma} | {idade} | {nota1} | {nota2}")

    print(count_A)
    print(count_B)
    print(count_C)