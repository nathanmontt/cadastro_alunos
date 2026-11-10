# Diário de bordo — Cadastro de alunos em CSV

## Data de início

09/11/2026

## O que eu quero descobrir?

- Qual turma é a mais predominante?
- Qual aluno com maior média?
- Qual a média das idades dos alunos?
- Qual(is) aluno(s) possui(em) maior nota na prova 1?
- Qual(is) aluno(s) possui(em) maior nota na prova 2?

## O que identifiquei ao abrir o CSV?

- Cabeçalho: informações ok, sem erros de formatação
- Delimitador: como é um arquivo `.csv`, o delimitador (`;`) estava correto
- Colunas numéricas: alguns valores estavam faltantes
- Colunas textuais: nomes com alguns erros de formatação básicos, ou faltantes
<!-- - Dúvidas e suspeitas: nenhuma -->

<!-- ## Regras que adotei

| Situação encontrada | Decisão | Justificativa |
|---|---|---|
| Exemplo: campo vazio | _preencher_ | _preencher_ | -->

## Erros encontrados no Python e como investiguei

| Sintoma / mensagem | O que tentei | O que aprendi |
|---|---|---|
| Nomes faltantes ou mal formatados | Verificação via `if/else` para olhar se era problema de falta de conteúdo ou erro de formatação | Aprimoramento no uso das condicionais e melhor uso dos *built-in methods* |
| Notas faltantes ou mal formatas | Verificação via `if/else` para olhar se era problema de falta de conteúdo ou erro de formatação | Aprimoramento no uso das condicionais e melhor uso dos *built-in methods*, como `.replace('','')` |
<!-- | _preencher_ | _preencher_ | _preencher_ | -->

<!-- ## Resultados que consegui verificar -->

<!-- _Preencher depois de terminar os cálculos._ -->

<!-- ## Melhorias futuras

_Preencher com ideias, como separar funções, exportar, testar etc._ -->
