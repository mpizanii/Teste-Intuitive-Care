import os
import tabula
import pandas as pd
import zipfile

def extrairArquivos(arquivo_zip, nome): #funcao para extrair o pdf do anexo 1
    try:
        with zipfile.ZipFile(arquivo_zip, 'r') as zipf:
            arquivos = zipf.namelist() #lista os nomes dos arquivos da pasta compactada
            for arquivo in arquivos:
                if nome in arquivo: 
                    zipf.extract(arquivo) #extrai o arquivo
                    print(f"Arquivo '{arquivo}' extraído com sucesso!")

                    return f"{arquivo}" 

            print(f"O arquivo '{nome}' não foi encontrado no zip.")
            return None
    except Exception as e:
        print(f"Erro ao processar o arquivo ZIP: {e}")
        return None

def compactarArquivos(arquivo, nome):
    with zipfile.ZipFile(f"{nome}.zip", "w") as zipf:
        zipf.write(arquivo) #escreve os arquivos na pasta.zip
    
    print(f"Arquivo compactado: {nome}.zip")

def extrairDados(pdf, pages):
    try:
        tabelas = tabula.read_pdf(pdf, pages=pages, multiple_tables=True, lattice=True) #le o pdf
        
        tabelasLimpas = [] 
        for tabela in tabelas:
            tabela.columns = [col.replace("\r", "").strip() for col in tabela.columns] #formata as colunas da tabela
            tabela = tabela.rename(columns={"OD": "Seg. Odontológica","AMB": "Seg. Ambulatorial"}) #renomeia as abreviações das colunas, conforme pedido no item 2.4

            tabelasLimpas.append(tabela) #adiciona as tabelas no array

        return tabelasLimpas
    
    except Exception as e:
        print(f"Erro ao extrair tabelas do arquivo '{pdf}': {e}")

        return None

def salvarCsv(lista, nome):
    try:
        tabelaCombinada = pd.concat(lista, ignore_index=True) #concatena as tabelas
        tabelaCombinada.to_csv(nome, index=False) #transforma em csv

        print(f"Tabelas combinadas salvas em '{nome}'")

    except Exception as e:
        print(f"Erro ao salvar o arquivo '{nome}': {e}")

def excluirArquivos(arquivos):
    for arquivo in arquivos:
        try:
            os.remove(arquivo) #remove os arquivos da raiz
            print(f"Arquivo removido com sucesso: {arquivo}")

        except FileNotFoundError:
            print(f"Arquivo não encontrado!")

        except Exception as e:
            print(f"Erro ao excluir o arquivo: {e}")

def main():
    arquivo_pdf = extrairArquivos('anexosCompactados.zip', 'anexo1.pdf') #extrai o anexo 1
    if not os.path.exists(arquivo_pdf):
        print(f"Erro: O arquivo '{arquivo_pdf}' não foi encontrado. Verifique o caminho e tente novamente.")
    else:
        listaTabelas = extrairDados(arquivo_pdf, pages='3-181') #extrai as tabelas das páginas onde possui os dados das tabelas
        salvarCsv(listaTabelas, "anexo1.csv") #salva como csv
        compactarArquivos("anexo1.csv", "Teste_Matheus_Pizani")
        arquivos = ["anexo1.pdf", "anexo1.csv"]
        excluirArquivos(arquivos) #exclui os arquivos da raiz

if __name__ == '__main__':
    main()