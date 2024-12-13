import os
import pandas as pd
from tabula import read_pdf
from openpyxl import Workbook

pdf_file = r"c:/Users/dejes/OneDrive/Área de Trabalho/Programação/projetos/Analise de dados/Painel Carteira 0128 VALEM-ADUFLA EST. 02-22  a .pdf"

# Lê todas as tabelas do PDF
tabelas = read_pdf(pdf_file, pages="all", multiple_tables=True, pandas_options={"header": None})

# Combinação e limpeza dos dados
df_final = pd.DataFrame()

for tabela in tabelas:
    df_final = pd.concat([df_final, tabela], ignore_index=True)

# Ajustar as colunas (ajustar manualmente)
colunas = [
    "Número de Usuários", "RECEITA", "DESPESA TOTAL", "DESPESA ASSISTENCIAL", 
    "Consultas", "Exames", "Despesas Hospitalares", "Intercambio", 
    "Opme", "Medicamento Oncológico", "Ressarcimento SUS", "Reembolso", 
    "Coparticipacao", "DESPESA NÃO ASSISTENCIAL", "RESULTADO", "SINISTRALIDADE"
]
df_final.columns = colunas[:len(df_final.columns)]

# diretório de saída
output_dir = r"C:/Users/dejes/OneDrive/Área de Trabalho/Programação/projetos/Analise de dados/Excel"  # Caminho completo
os.makedirs(output_dir, exist_ok=True)  # Cria o diretório se não existir

# diretório especificado
output_file = os.path.join(output_dir, "dados_extraidos.xlsx")
df_final.to_excel(output_file, index=False)

print(f"Arquivo Excel criado e salvo no diretório: {output_dir}")
