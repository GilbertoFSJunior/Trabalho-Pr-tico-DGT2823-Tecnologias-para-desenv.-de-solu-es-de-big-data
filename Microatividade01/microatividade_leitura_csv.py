# Microatividade 1: Descrever como ler um arquivo CSV usando a biblioteca Pandas
# Analista de Dados - Leitura de dados externos

# PROCEDIMENTO 2.1: Importe a biblioteca pandas
import pandas as pd
import os
import sys

print("=== MICROATIVIDADE 1: LEITURA DE ARQUIVO CSV COM PANDAS ===\n")
print("✓ Passo 2.1: Biblioteca pandas importada com sucesso")

# PROCEDIMENTO 2.2: Cria uma variável
dados_lidos = None
print("✓ Passo 2.2: Variável 'dados_lidos' criada")

# PROCEDIMENTO 2.3 e 2.4: Leia o conteúdo do arquivo CSV e atribua à variável
print("\n--- LEITURA DO ARQUIVO CSV ---")

# Carrega o arquivo 'dados.csv' localizado no mesmo diretório que este script
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'dados.csv')

try:
	dados_lidos = pd.read_csv(csv_path, sep=';', engine='python', encoding='utf-8')
	print("✓ Passo 2.3 e 2.4: Arquivo CSV lido e dados atribuídos à variável 'dados_lidos'")
except FileNotFoundError:
	print(f"Erro: arquivo não encontrado em: {csv_path}")
	print("Verifique se 'dados.csv' está no mesmo diretório do script e tente novamente.")
	sys.exit(1)
except Exception as e:
	print(f"Erro ao ler o CSV: {e}")
	sys.exit(1)

# Informações sobre os parâmetros utilizados
print("\n--- PARÂMETROS UTILIZADOS NA LEITURA ---")
print("• sep=';'        → Define o separador de colunas como ponto e vírgula")
print("• engine='python' → Especifica o motor de análise Python")
print("• encoding='utf-8' → Define a codificação de caracteres")

# PROCEDIMENTO 2.5: Imprima/exiba em tela os dados da variável
print("\n--- PASSO 2.5: LEITURA EEXIBIÇÃO DOS DADOS ---")

print("=== DADOS DO ARQUIVO CSV ===")
print(dados_lidos)

print("\n=== INFORMAÇÕES SOBRE OS DADOS ===")
print(f"Formato do DataFrame: {dados_lidos.shape}")
print(f"Colunas: {list(dados_lidos.columns)}")
print(f"Tipos de dados:")
print(dados_lidos.dtypes)

print("\n=== EXIBINDO PRIMEIRAS 5 LINHAS ===")
print(dados_lidos.head())

print("\n=== EXIBINDO ÚLTIMAS 5 LINHAS ===")
print(dados_lidos.tail())

print("\n=== RESUMO DE ESTATÍSTICAS BÁSICAS ===")
print(dados_lidos.describe())

print("\n=== MICROATIVIDADE -> CONCLUÍDA COM SUCESSO! ===")
print("Biblioteca pandas importada com sucesso")
print("Variável criada com sucesso")
print("Arquivo CSV lido com parâmetros especificados ")
print("Dados atribuídos à variável")
print("Conteúdo exibido em tela")
