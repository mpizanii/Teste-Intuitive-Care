# Criei esse arquivo .py pois alguns dados em determinadas tabelas estavam causando inconsistencias no banco de dados
import pandas as pd
import csv
import os

def alterarFormatoDate(arquivo, nomeNovoArquivo):
    df = pd.read_csv(arquivo, on_bad_lines='skip', sep=';')
    
    df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

    df.to_csv(nomeNovoArquivo, index=False, sep=';', quotechar='"', quoting=csv.QUOTE_ALL)

def alterarFormatoFloat(arquivo, nomeNovoArquivo):
    df = pd.read_csv(arquivo, on_bad_lines='skip', sep=';')
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    full_path = os.path.join(downloads_path, nomeNovoArquivo)

    df['VL_SALDO_INICIAL'] = df['VL_SALDO_INICIAL'].str.replace(',', '.').astype(float)
    df['VL_SALDO_FINAL'] = df['VL_SALDO_FINAL'].str.replace(',', '.').astype(float)

    df.to_csv(full_path, index=False, sep=';', quotechar='"', quoting=csv.QUOTE_ALL)

    print(f"Arquivo {nomeNovoArquivo} salvo na pasta {downloads_path}")

def excluirArquivos(arquivo):
    try:
        os.remove(arquivo) #remove os arquivos da raiz
        print(f"Arquivo removido: {arquivo}")

    except FileNotFoundError:
        print(f"Arquivo não encontrado! {arquivo}")

    except Exception as e:
        print(f"Erro ao excluir o arquivo: {e}")

def main():
    alterarFormatoDate('Teste de banco de dados/Arquivos/4T2023.csv', '4T2023SemiCorrigido.csv')
    alterarFormatoFloat('Teste de banco de dados/Arquivos/1T2023.csv', '1T2023Corrigido.csv')
    alterarFormatoFloat('Teste de banco de dados/Arquivos/1T2024.csv', '1T2024Corrigido.csv')
    alterarFormatoFloat('Teste de banco de dados/Arquivos/2T2023.csv', '2T2023Corrigido.csv')
    alterarFormatoFloat('Teste de banco de dados/Arquivos/2T2024.csv', '2T2024Corrigido.csv')
    alterarFormatoFloat('Teste de banco de dados/Arquivos/3T2023.csv', '3T2023Corrigido.csv')
    alterarFormatoFloat('Teste de banco de dados/Arquivos/3T2024.csv', '3T2024Corrigido.csv')
    alterarFormatoFloat('4T2023SemiCorrigido.csv', '4T2023Corrigido.csv')
    excluirArquivos('4T2023SemiCorrigido.csv')
    alterarFormatoFloat('Teste de banco de dados/Arquivos/4T2024.csv', '4T2024Corrigido.csv')

if __name__ == '__main__':
    main()
