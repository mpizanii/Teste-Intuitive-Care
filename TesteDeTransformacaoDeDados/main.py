import os
import tabula
import pandas as pd
import zipfile

def extrair_arquivos(arquivo_zip, nome):  
    try:
        with zipfile.ZipFile(arquivo_zip, 'r') as zipf:
            arquivos = zipf.namelist()  
            for arquivo in arquivos:
                if nome in arquivo:
                    zipf.extract(arquivo)  
                    print(f"Arquivo '{arquivo}' extraído com sucesso!")
                    return f"{arquivo}"
            print(f"O arquivo '{nome}' não foi encontrado no zip.")
            return None
    except zipfile.BadZipFile as e:  
        print(f"Erro: Arquivo ZIP inválido ou corrompido - {e}")
        return None
    except Exception as e:
        print(f"Erro ao processar o arquivo ZIP: {e}")
        return None

def compactar_arquivos(arquivo, nome): 
    try:  
        with zipfile.ZipFile(f"{nome}.zip", "w") as zipf:
            if os.path.exists(arquivo):  
                zipf.write(arquivo) 
            else:
                print(f"Erro: Arquivo '{arquivo}' não encontrado para compactação.")
        print(f"Arquivo compactado: {nome}.zip")
    except Exception as e:
        print(f"Erro ao compactar arquivo: {e}")

def extrair_dados(pdf, pages): 
    try:
        tabelas = tabula.read_pdf(pdf, pages=pages, multiple_tables=True, lattice=True) 

        tabelas_limpas = []
        for tabela in tabelas:
            tabela.columns = [col.replace("\r", "").strip() for col in tabela.columns]  
            tabela = tabela.rename(columns={"OD": "Seg. Odontológica", "AMB": "Seg. Ambulatorial"}) 

            tabelas_limpas.append(tabela) 

        return tabelas_limpas
    except FileNotFoundError: 
        print(f"Erro: O arquivo '{pdf}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao extrair tabelas do arquivo '{pdf}': {e}")
        return None

def salvar_csv(lista, nome):  
    try:
        tabela_combinada = pd.concat(lista, ignore_index=True)  
        tabela_combinada.to_csv(nome, index=False)  

        print(f"Tabelas combinadas salvas em '{nome}'")
    except ValueError as e:  
        print(f"Erro: Lista de tabelas está vazia - {e}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo '{nome}': {e}")

def excluir_arquivos(arquivos):  
    for arquivo in arquivos:
        try:
            os.remove(arquivo) 
            print(f"Arquivo removido com sucesso: {arquivo}")
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {arquivo}")
        except Exception as e:
            print(f"Erro ao excluir o arquivo '{arquivo}': {e}")

def main():
    arquivo_pdf = extrair_arquivos('anexosCompactados.zip', 'anexo1.pdf') 
    if not arquivo_pdf: 
        print(f"Erro: O arquivo '{arquivo_pdf}' não foi encontrado. Verifique o caminho e tente novamente.")
    else:
        lista_tabelas = extrair_dados(arquivo_pdf, pages='3-181')  
        if lista_tabelas:  
            salvar_csv(lista_tabelas, "anexo1.csv")  
            compactar_arquivos("anexo1.csv", "Teste_Matheus_Pizani")  
            arquivos = ["anexo1.pdf", "anexo1.csv"]
            excluir_arquivos(arquivos)  

if __name__ == '__main__':
    main()