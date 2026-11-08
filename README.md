# Cadastro de alunos em CSV

> Leitura básica e estruturação de registros  
> Projeto de aprendizado em Python puro (biblioteca padrão), com dados fictícios e intencionalmente imperfeitos gerados via IA

## Contexto

Uma escola fictícia disponibilizou uma lista de alunos. Você precisa ler o CSV e produzir um resumo simples para a coordenação, sem alterar o arquivo original.

## Objetivo

Construir, **por conta própria**, um programa de linha de comando que transforme os arquivos brutos em informações úteis, com critérios explícitos de tratamento de dados.

## Ferramentas previstas

- Linguagem: Python 3
- Editor: VS Code

## Arquivos de entrada

Veja os arquivos na pasta `dados/brutos/`. Leia-os como **texto CSV separado por `;`**. Não modifique o conteúdo original para fazer seu código funcionar.

## Requisitos do projeto

- [ ] Abrir o arquivo CSV e reconhecer o cabeçalho.
- [ ] Inspecionar pelo menos cinco registros e verificar seus tipos.
- [ ] Identificar campos vazios ou valores que não parecem notas válidas.
- [ ] Definir uma regra para calcular uma média quando faltam notas, sem inventar números.
- [ ] Separar registros que podem ser calculados dos que precisam de revisão.
- [ ] Exibir um resumo legível no terminal e registrar observações no diário.

## Perguntas que a análise deve ajudar a responder

- Quantos cadastros possuem notas utilizáveis?
- Que tipos de problema impedem calcular uma média?
- Qual turma apresenta maior média, considerando somente registros válidos?

## Como executar

Abra o terminal na raiz deste projeto e execute `python src/main.py` (ou `py src/main.py` no Windows).

## Saídas esperadas

- Um resumo legível no terminal.
- Um registro das decisões de limpeza em `docs/DIARIO.md`.

## Estrutura

```text
Código principal: src/main.py
Dados brutos: dados/brutos/
Diário de bordo: docs/DIARIO.md
```

## Nota sobre os dados

Todos os dados são sintéticos, produzidos exclusivamente para estudo. Não contêm dados reais de clientes, alunos ou empresas.