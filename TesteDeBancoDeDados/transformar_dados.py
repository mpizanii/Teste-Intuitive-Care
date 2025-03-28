# Criei esse arquivo .py pois alguns dados em determinadas tabelas estavam causando inconsistencias no banco de dados
import pandas as pd
import csv
import os

def alterar_formato_date(arquivo, nome_novo_arquivo):  
    try:  
        df = pd.read_csv(arquivo, on_bad_lines='skip', sep=';')

        if 'DATA' in df.columns: 
            df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
        else:
            raise KeyError("A coluna 'DATA' não foi encontrada no arquivo.") 

        df.to_csv(nome_novo_arquivo, index=False, sep=';', quotechar='"', quoting=csv.QUOTE_ALL)
        print(f"Arquivo '{nome_novo_arquivo}' salvo com sucesso.")
    except Exception as e:
        print(f"Erro ao alterar o formato da data no arquivo '{arquivo}': {e}")

def alterar_formato_float(arquivo, nome_novo_arquivo):  
    try:
        df = pd.read_csv(arquivo, on_bad_lines='skip', sep=';')
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        full_path = os.path.join(downloads_path, nome_novo_arquivo)

        colunas_float = ['VL_SALDO_INICIAL', 'VL_SALDO_FINAL']
        for coluna in colunas_float:
            if coluna not in df.columns:
                raise KeyError(f"A coluna '{coluna}' não foi encontrada no arquivo.")

        df['VL_SALDO_INICIAL'] = df['VL_SALDO_INICIAL'].str.replace(',', '.').astype(float)
        df['VL_SALDO_FINAL'] = df['VL_SALDO_FINAL'].str.replace(',', '.').astype(float)

        df.to_csv(full_path, index=False, sep=';', quotechar='"', quoting=csv.QUOTE_ALL)
        print(f"Arquivo '{nome_novo_arquivo}' salvo na pasta {downloads_path}")
    except Exception as e:
        print(f"Erro ao alterar o formato float no arquivo '{arquivo}': {e}")

def excluir_arquivos(arquivo): 
    try:
        os.remove(arquivo)  
        print(f"Arquivo removido: {arquivo}")
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {arquivo}")
    except Exception as e:
        print(f"Erro ao excluir o arquivo '{arquivo}': {e}")

def main():
    try:  
        alterar_formato_date('TesteDeBancoDeDados/Arquivos/4T2023.csv', '4T2023SemiCorrigido.csv')
        alterar_formato_float('TesteDeBancoDeDados/Arquivos/1T2023.csv', '1T2023Corrigido.csv')
        alterar_formato_float('TesteDeBancoDeDados/Arquivos/1T2024.csv', '1T2024Corrigido.csv')
        alterar_formato_float('TesteDeBancoDeDados/Arquivos/2T2023.csv', '2T2023Corrigido.csv')
        alterar_formato_float('TesteDeBancoDeDados/Arquivos/2T2024.csv', '2T2024Corrigido.csv')
        alterar_formato_float('TesteDeBancoDeDados/Arquivos/3T2023.csv', '3T2023Corrigido.csv')
        alterar_formato_float('TesteDeBancoDeDados/Arquivos/3T2024.csv', '3T2024Corrigido.csv')
        alterar_formato_float('4T2023SemiCorrigido.csv', '4T2023Corrigido.csv')
        excluir_arquivos('4T2023SemiCorrigido.csv')
        alterar_formato_float('TesteDeBancoDeDados/Arquivos/4T2024.csv', '4T2024Corrigido.csv')
    except Exception as e:
        print(f"Erro durante a execução do fluxo principal: {e}")

if __name__ == '__main__':
    main()