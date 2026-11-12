from pathlib import Path
import csv

caminho_csv = Path(__file__).parent.parent / "dados" / "brutos" / "alunos.csv"


def converter_float(valor_texto: str) -> float:
    valor_texto = valor_texto.strip().casefold()
    if not valor_texto or valor_texto == "ausente":
        return 0.0

    return float(valor_texto.replace(',','.'))

def preparar_nome(nome_texto: str) -> str:
    nome = nome_texto.strip().title()

def imprimir_cabecalho() -> None:
    print(
        f"{'MATRÍCULA':<12}"
        f"{'NOME':<25}"
        f"{'TURMA':<8}"
        f"{'IDADE':<12}"
        f"{'NOTA 1':>10}"
        f"{'NOTA 2':>10}"
        f"{'FREQUÊNCIA':>14}"
    )
    print("-" * 91)

def converter_idade(idade_texto: str):
    idade = idade_texto.strip().casefold()

    idades_por_extenso = {
        "dezesseis": 16,
    }

    if idade.isdigit():
        return int(idade)

    if idade in idades_por_extenso:
        return idades_por_extenso[idade]

    return "SEM IDADE"

with caminho_csv.open("r", encoding="utf-8-sig", newline="") as arq:
    leitor = csv.DictReader(arq, delimiter=";")
    count_A = 0
    count_B = 0
    count_C = 0

    imprimir_cabecalho()

    for each_line in leitor:
        matricula = each_line["matricula"]
        nome = preparar_nome(each_line["nome"])
        turma = each_line["turma"]
        idade = converter_idade(each_line["idade"])

        nota1 = converter_float(each_line["nota1"])
        nota2 = converter_float(each_line["nota2"])

        # ---------------------------------------
        # verificação de frequencia
        frequencia_pct_texto = each_line["frequencia_pct"].strip()
        if not frequencia_pct_texto:
            frequencia_pct = float(0)
        else:
            frequencia_pct = float(frequencia_pct_texto.replace(',','.'))


        # ---------------------------------------
        # verificação de turma predominante
        if turma == 'A':
            count_A += 1
        elif turma == 'B':
            count_B += 1
        elif turma == 'C':
            count_C += 1

        # print dos valores
        print(f"{matricula} | {nome} | {turma} | {idade} | {nota1} | {nota2} | {frequencia_pct:.2f}%")
        print("-" * 48)

    print(count_A)
    print(count_B)
    print(count_C)