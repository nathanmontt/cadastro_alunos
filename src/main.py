from pathlib import Path
import csv
import statistics as sc

caminho_csv = Path(__file__).parent.parent / "dados" / "brutos" / "alunos.csv"

def converter_float(valor: str) -> float:
    valor = valor.strip().casefold()
    if not valor or valor == "ausente":
        return 0.0

    valor2 = float(valor.replace(",","."))
    if valor2 < 0:
        return 0.0

    return float(valor.replace(",","."))

def preparar_nome(valor: str) -> str:
    nome = valor.strip().title()

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

def preparar_nome(valor: str) -> str:
    nome = valor.strip().title()

    return nome or "SEM REGISTRO"

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
        f"{nome:<25}"
        f"{turma:<8}"
        f"{str(idade):<12}"
        f"{nota1:>10.2f}"
        f"{nota2:>10.2f}"
        f"{frequencia:>13.2f}%"
    )

with caminho_csv.open("r", encoding="utf-8-sig", newline="") as arq:
    leitor = csv.DictReader(arq, delimiter=";")
    qntd_turma = {
        "A": 0,
        "B": 0,
        "C": 0,
    }

    imprimir_cabecalho()
    media_nota1 = []
    media_nota2 = []

    media_idade = []

    for each_line in leitor:
        matricula = each_line["matricula"]
        nome = preparar_nome(each_line["nome"])
        turma = each_line["turma"].strip().upper()
        idade = converter_idade(each_line["idade"])
        media_idade.append(idade)

        nota1 = converter_float(each_line["nota1"])
        nota2 = converter_float(each_line["nota2"])
        media_nota1.append(nota1)
        media_nota2.append(nota2)

        frequencia = converter_float(each_line["frequencia_pct"])

        # ESTATÍSTICAS
        # verificação de turma predominante
        if turma in qntd_turma:
            qntd_turma[turma] += 1

        imprimir_aluno(matricula, nome, turma, idade, nota1, nota2, frequencia)

    idades_validas = [idade for each_age in media_idade if isinstance(each_age, (int, float))]

    print()
    print("-" * 91)
    print("\nESTATÍSTICAS")

    turma_predom = max(qntd_turma, key=qntd_turma.get)
    holder_media_nota1 = sc.mean(media_nota1)
    holder_media_nota2 = sc.mean(media_nota2)
    media_idade = sc.mean(idades_validas) if idades_validas else 0

    print(f"{'TURMA PREDOMINANTE'} | {'MAIOR MÉDIA'} | {'MÉDIA DE IDADES'}")
    print(f"{holder_media_nota1:>11.1f} {'|':>8} {holder_media_nota2:>8.1f} {'|':>4} {media_idade:>8}")

    # print(f"Turma predominante: {turma_predom} ({qntd_turma[turma_predom]} alunos)")

    # if qntd_turma["A"] > qntd_turma["B"] and qntd_turma["A"] > qntd_turma["C"]:
    #     print(f"A: {qntd_turma["A"]}")
    # elif qntd_turma["B"] > qntd_turma["A"] and qntd_turma["B"] > qntd_turma["C"]:
    #     print(f"B: {qntd_turma["B"]}")
    # elif qntd_turma["C"] > qntd_turma["A"] and qntd_turma["C"] > qntd_turma["B"]:
    #     print(f"C: {qntd_turma["C"]}")
    
    # print(qntd_turma["A"], qntd_turma["B"], qntd_turma["C"])