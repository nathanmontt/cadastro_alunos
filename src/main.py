from pathlib import Path
import csv

caminho_csv = Path(__file__).parent.parent / "dados" / "brutos" / "alunos.csv"


def converter_float(valor: str) -> float:
    valor = valor.strip().casefold()
    if not valor or valor == "ausente":
        return 0.0

    return float(valor.replace(",","."))

def preparar_nome(valor: str) -> str:
    nome = valor.strip().title()

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

def imprimir_aluno(matricula: str, nome: str, turma: str, idade, nota1: float, nota2: float, frequencia: float,) -> None:
    print(
        f"{matricula:<12}"
        f"{nome}"
        f"{turma:<8}"
        f"{str(idade):<12}"
        f"{nota1:>10.2f}"
        f"{nota2:>10.2f}"
        f"{frequencia:>13.2f}%"
    )

def converter_idade(valor: str):
    valor = valor.strip().casefold()

    idades_por_extenso = {
        "dezesseis": 16,
    }

    if valor.isdigit():
        return int(valor)

    if valor in idades_por_extenso:
        return idades_por_extenso[valor]

    return "SEM IDADE"

with caminho_csv.open("r", encoding="utf-8-sig", newline="") as arq:
    leitor = csv.DictReader(arq, delimiter=";")
    quantidade_turmas = {
        "A": 0,
        "B": 0,
        "C": 0,
    }

    imprimir_cabecalho()

    for each_line in leitor:
        matricula = each_line["matricula"]
        nome = preparar_nome(each_line["nome"])
        turma = each_line["turma"].strip().upper()
        idade = converter_idade(each_line["idade"])

        nota1 = converter_float(each_line["nota1"])
        nota2 = converter_float(each_line["nota2"])

        frequencia = converter_float(each_line["frequencia_pct"])

        # ESTATÍSTICAS
        # verificação de turma predominante
        if turma in quantidade_turmas:
            quantidade_turmas[turma] += 1

        imprimir_aluno(matricula, nome, turma, idade, nota1, nota2, frequencia)