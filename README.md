# 💻 DGT2823 - Tecnologias para Desenvolvimento de Soluções de Big Data

Este repositório contém o trabalho prático (Missão Prática | Mundo 5 | Nível 5) da disciplina DGT2823, focado em **Análise e Limpeza de Dados** utilizando a biblioteca **Pandas** da linguagem Python.

O objetivo principal foi demonstrar proficiência no tratamento de um conjunto de dados brutos e inconsistentes, simulando um cenário real de Big Data.

---

## 🎯 Objetivos do Projeto

### Objetivos Gerais
* [cite_start]Aplicar técnicas de manipulação de dados utilizando a biblioteca Pandas[cite: 1382].
* [cite_start]Realizar a limpeza e o tratamento de dados inconsistentes e ausentes[cite: 1383, 1367].
* [cite_start]Demonstrar proficiência em análise exploratória de dados (EDA)[cite: 1384].

### Principais Habilidades Demonstradas
* [cite_start]Leitura de arquivos CSV[cite: 1386].
* [cite_start]Criação de subconjuntos de dados (data subsetting)[cite: 1387].
* [cite_start]Configuração de opções de visualização de DataFrames[cite: 1388].
* [cite_start]Tratamento de valores nulos e inconsistentes[cite: 1390].
* [cite_start]Conversão e validação de tipos de dados[cite: 1391, 1392].

---

## 📊 Dataset Utilizado

[cite_start]O conjunto de dados simula registros de atividades físicas e foi **propositadamente criado com inconsistências** para o exercício de limpeza[cite: 1376].

| Coluna | Tipo Original | Variável | Problemas Identificados |
| :--- | :--- | :--- | :--- |
| `ID` | `int64` | Identificador Único | - |
| `Duration` | `int64` | Duração da Atividade (min) | - |
| `Date` | `object` (string) | Data da Atividade | [cite_start]1 valor nulo (NaN) e 1 formato inconsistente ("20201226")[cite: 1418, 1419]. |
| `Pulse` | `int64` | Frequência Cardíaca Média | - |
| `Maxpulse` | `int64` | Frequência Cardíaca Máxima | - |
| `Calories` | `float64` | Calorias Queimadas | [cite_start]2 valores nulos (NaN)[cite: 1418]. |

- [cite_start]**Dimensões do Dataset Original:** 32 linhas e 6 colunas[cite: 1401].
- [cite_start]**Ambiente:** Python 3.13.3, Pandas, Visual Studio Code[cite: 1395, 1396, 1397].

---

## 🔬 Microatividades (Exploração de Dados)

As microatividades focaram na demonstração de comandos essenciais do Pandas para a análise exploratória.

### 1. Leitura de CSV (`pd.read_csv`)
[cite_start]Demonstração da leitura de arquivos CSV com a função `pd.read_csv()`, especificando parâmetros como separador (`;`) e codificação (`utf-8`)[cite: 1451, 1530, 1531].

### 2. Criação de Subconjuntos
[cite_start]Criação de um novo DataFrame (`subconjunto_dados`) selecionando apenas as colunas `['ID', 'Duration', 'Pulse']`, reduzindo as colunas de 6 para 3, mantendo 32 linhas[cite: 1653, 1826, 1969].

### 3. Configuração de Visualização
[cite_start]Uso do comando `pd.set_option('display.max_rows', 9999)` para garantir que todo o dataset (32 linhas) fosse exibido no terminal, evitando o truncamento[cite: 1992, 2017].

### 4. Visualização de Linhas
[cite_start]Utilização dos métodos `.head(10)` e `.tail(10)` para exibir as primeiras e últimas 10 linhas do DataFrame[cite: 2045, 2054, 2180, 2181].

### 5. Informações Gerais
Extração de metadados e estatísticas do DataFrame com os métodos:
* [cite_start]**`.info()`**: Detalhamento de colunas, contagens não nulas e uso de memória (1.6+ KB)[cite: 2212, 2363].
* [cite_start]**`.isnull().sum()`**: Confirmação de 1 nulo em `Date` e 2 nulos em `Calories` (Total de 3 valores ausentes)[cite: 2371, 2350, 2360].
* [cite_start]**`.describe()`**: Geração de um resumo estatístico para colunas numéricas[cite: 2309, 2394].

---

## ✅ Limpeza e Tratamento de Dados (Passos 7 - 12)

A seção final focou na transformação do dataset inconsistente em um conjunto de dados limpo e estruturado (`dados_tratados`).

| Passo | Descrição | Comando Pandas Principal | Resultado |
| :--- | :--- | :--- | :--- |
| **Passo 7** | [cite_start]Tratamento de valores nulos em `Calories`[cite: 2463]. | [cite_start]`dados_tratados['Calories'].fillna(0, inplace=True)`[cite: 2471]. | Valores `NaN` substituídos por `0`. |
| **Passo 8-9** | Substituição inicial de nulos em `Date` e correção para `NaN` (para forçar o tipo `datetime`). | [cite_start]`dados_tratados['Date'].replace('1900/01/01', np.nan)`[cite: 2531]. | Nulo em `Date` preparado para ser convertido para `NaT`. |
| **Passo 10** | [cite_start]Correção do formato de data inconsistente (`20201226`)[cite: 2555]. | [cite_start]`dados_tratados['Date'].replace(20201226, '2020/12/26')`[cite: 2577]. | Formato corrigido para `YYYY/MM/DD`. |
| **Passo 11** | [cite_start]Conversão final da coluna `Date` para o tipo `datetime`[cite: 2580]. | [cite_start]`pd.to_datetime(..., format='%Y/%m/%d', errors='coerce')`[cite: 2592]. | [cite_start]Coluna `Date` passa de `object` para `datetime64[ns]`[cite: 2662]. |
| **Passo 12** | [cite_start]Remoção de registros com nulos (`NaT`) restantes na coluna `Date`[cite: 2604]. | [cite_start]`dados_tratados.dropna(subset=['Date'])`[cite: 2628]. | [cite_start]Remoção da Linha 22, resultando em um DataFrame final com **31 linhas**[cite: 2673, 2679]. |

### Resumo Final

O processo demonstrou a capacidade de lidar com diferentes problemas de qualidade de dados (nulos, formatos inconsistentes e tipos incorretos) de forma estruturada.

> [cite_start]🌟 **Conjunto de Dados Final:** 31 linhas limpas[cite: 2673].
> 
> [cite_start]Valores nulos em 'Calories' substituídos por 0[cite: 2675].
> 
> [cite_start]Coluna 'Date' convertida para o formato `datetime`[cite: 2677].

[cite_start][Link para o Código no GitHub: **{{Cole o link do anexo aqui}}**](https://github.com/GilbertoFS.Junior/Trabalho-Pr-tico-DGT2823-Tecnologias-para-desenv.-de-solu-es-de-big-data.git)
