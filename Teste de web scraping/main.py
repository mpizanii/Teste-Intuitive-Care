import wget
import zipfile
import os
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def iniciarNavegador():
    options = Options()
    options.add_argument("--headless") #sem interface gráfica
    options.add_argument("--disable-gpu") #desativa GPU
    options.add_argument("--no-sandbox") #evita problemas de permissões

    servico = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=servico, options=options)

def obterUrl(navegador, xpath, indice):
    elemento = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))) #espera a pagina disponibilizar o elemento
    elemento.click()

    abas = navegador.window_handles
    if indice < len(abas):
        navegador.switch_to.window(abas[indice]) #navega até a aba aberta
        url = navegador.current_url

        if not url.startswith("http"):
            raise ValueError(f"URL inválida: {url}") #erro caso capture uma url inválida

        navegador.close() #fecha a aba
        return url #retorna a url da página
    else:
        raise IndexError(f"Não há abas suficientes para o índice {indice}.")

def baixarPdf(url, nomeArquivo):
    resposta = requests.get(url, stream=True)
    if resposta.status_code == 200:
        with open(f"{nomeArquivo}.pdf", "wb") as f:
            for chunk in resposta.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f"Download concluído: {nomeArquivo}.pdf")
    else:
        print(f"Erro ao baixar {nomeArquivo}: Status {resposta.status_code}")  

def compactarArquivos(arquivos, nome):
    with zipfile.ZipFile(f"{nome}.zip", "w") as zipf:
        for arquivo in arquivos:
            zipf.write(arquivo) #escreve os arquivos na pasta.zip
    
    print(f"Arquivo compactado: {nome}.zip")

def excluirArquivos(arquivos):
    for arquivo in arquivos:
        try:
            os.remove(arquivo) #remove os arquivos da raiz
            print(f"Arquivo removido: {arquivo}")

        except FileNotFoundError:
            print(f"Arquivo não encontrado! {arquivo}")

        except Exception as e:
            print(f"Erro ao excluir o arquivo: {e}")

def voltarAbaprincipal(navegador):
    navegador.switch_to.window(navegador.window_handles[0])

def main():
    navegador = iniciarNavegador()

    try:
        url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'
        navegador.get(url)
        navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div[2]/button[3]').click() #aceitar cookies

        urlAnexo1 = obterUrl(navegador, '//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[1]/a[1]', 1) #capturar anexo 1
        voltarAbaprincipal(navegador)

        urlAnexo2 = obterUrl(navegador, '//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[2]/a', 1) #capturar anexo 2
        voltarAbaprincipal(navegador)

        baixarPdf(urlAnexo1, 'anexo1')
        print("\nAnexo 1 baixado!")

        baixarPdf(urlAnexo2, 'anexo2')
        print("\nAnexo 2 baixado!")

        arquivos = ["anexo1.pdf", "anexo2.pdf"]
        compactarArquivos(arquivos, "anexosCompactados")
        excluirArquivos(arquivos)
        
    except Exception as e:
        print(f"Erro durante a execução: {e}")
    finally:
        navegador.quit() #fecha navegador
        
if __name__ == '__main__':
    main()