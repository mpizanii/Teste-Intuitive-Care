import wget
import zipfile
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_argument("--headless") #sem interface gráfica
CHROME_OPTIONS.add_argument("--disable-gpu") #desativa GPU
CHROME_OPTIONS.add_argument("--no-sandbox") #evita problemas de permissões

SERVICO = Service(ChromeDriverManager().install())
NAVEGADOR = webdriver.Chrome(service=SERVICO, options=CHROME_OPTIONS)

def obterUrl(xpath, indice):
    elemento = WebDriverWait(NAVEGADOR, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))) #espera a pagina disponibilizar o elemento
    elemento.click()

    abas = NAVEGADOR.window_handles
    if indice < len(abas):
        NAVEGADOR.switch_to.window(abas[indice]) #navega até a aba aberta
        url = NAVEGADOR.current_url

        if not url.startswith("http"):
            raise ValueError(f"URL inválida: {url}") #erro caso capture uma url inválida

        NAVEGADOR.close() #fecha a aba
        return url #retorna a url da página
    else:
        raise IndexError(f"Não há abas suficientes para o índice {indice}.")

def baixarPdf(url, nomeArquivo):
    pdf = wget.download(url, f'{nomeArquivo}.pdf')
    return pdf

def voltarAbaprincipal():
    NAVEGADOR.switch_to.window(NAVEGADOR.window_handles[0])

def compactarArquivos(arquivos, nome):
    with zipfile.ZipFile(f"{nome}.zip", "w") as zipf:
        for arquivo in arquivos:
            zipf.write(arquivo) #escreve os arquivos na pasta.zip
    
    print(f"Arquivo compactado: {nome}.zip")

def excluirArquivos(arquivos):
    for arquivo in arquivos:
        try:
            os.remove(arquivo) #remove os arquivos da raiz
            print(f"Arquivo removido com sucesso: {arquivo}")

        except FileNotFoundError:
            print(f"Arquivo não encontrado!")

        except Exception as e:
            print(f"Erro ao excluir o arquivo: {e}")

if __name__ == '__main__':
    try:
        url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'
        NAVEGADOR.get(url)
        NAVEGADOR.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div[2]/button[3]').click() #aceitar cookies

        urlAnexo1 = obterUrl('//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[1]/a[1]', 1) #capturar anexo 1
        voltarAbaprincipal()

        urlAnexo2 = obterUrl('//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[2]/a', 1) #capturar anexo 2
        voltarAbaprincipal()

        baixarPdf(urlAnexo1, 'anexo1')
        print("\nAnexo 1 baixado!")

        baixarPdf(urlAnexo2, 'anexo2')
        print("\nAnexo 2 baixado!")

        arquivos = ["anexo1.pdf", "anexo2.pdf"]
        nome = "anexosCompactados"

        compactarArquivos(arquivos, nome)
        excluirArquivos(arquivos)
        
    except Exception as e:
        print(f"Erro durante a execução: {e}")
    finally:
        NAVEGADOR.quit() #fecha NAVEGADOR