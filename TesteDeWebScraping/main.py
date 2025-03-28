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

def iniciar_navegador():
    options = Options()
    options.add_argument("--headless")  # sem interface gráfica
    options.add_argument("--disable-gpu")  # desativa GPU
    options.add_argument("--no-sandbox")  # evita problemas de permissões

    try: 
        servico = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=servico, options=options)
    except Exception as e:
        raise RuntimeError(f"Erro ao iniciar o navegador: {e}")

def obter_url(navegador, xpath, indice):
    try:
        elemento = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))  # espera o elemento
        elemento.click()

        abas = navegador.window_handles
        if indice < len(abas):
            navegador.switch_to.window(abas[indice])  # navega até a aba aberta
            url = navegador.current_url

            if not url.startswith("http"):
                raise ValueError(f"URL inválida: {url}")  # erro caso capture uma url inválida

            navegador.close()  # fecha a aba
            return url  # retorna a url da página
        else:
            raise IndexError(f"Não há abas suficientes para o índice {indice}.")
    except Exception as e: 
        raise RuntimeError(f"Erro ao obter URL: {e}")

def baixar_pdf(url, nome_arquivo):  
    try:  
        resposta = requests.get(url, stream=True)
        resposta.raise_for_status()  
        with open(f"{nome_arquivo}.pdf", "wb") as f:
            for chunk in resposta.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f"Download concluído: {nome_arquivo}.pdf")
    except requests.RequestException as e:
        print(f"Erro ao baixar {nome_arquivo}: {e}")

def compactar_arquivos(arquivos, nome): 
    try:  
        with zipfile.ZipFile(f"{nome}.zip", "w") as zipf:
            for arquivo in arquivos:
                if os.path.exists(arquivo):  
                    zipf.write(arquivo)  # escreve os arquivos no .zip
        print(f"Arquivo compactado: {nome}.zip")
    except Exception as e:
        print(f"Erro ao compactar arquivos: {e}")

def excluir_arquivos(arquivos):  
    for arquivo in arquivos:
        try:
            os.remove(arquivo)  # remove os arquivos da raiz
            print(f"Arquivo removido: {arquivo}")
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {arquivo}")
        except Exception as e:
            print(f"Erro ao excluir o arquivo {arquivo}: {e}")

def voltar_aba_principal(navegador): 
    navegador.switch_to.window(navegador.window_handles[0])

def main():
    navegador = iniciar_navegador()

    try:
        url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'
        navegador.get(url)
        navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div[2]/button[3]').click()  # aceitar cookies

        url_anexo1 = obter_url(navegador, '//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[1]/a[1]', 1)  # capturar anexo 1
        voltar_aba_principal(navegador)

        url_anexo2 = obter_url(navegador, '//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[2]/a', 1)  # capturar anexo 2
        voltar_aba_principal(navegador)

        baixar_pdf(url_anexo1, 'anexo1')
        print("\nAnexo 1 baixado!")

        baixar_pdf(url_anexo2, 'anexo2')
        print("\nAnexo 2 baixado!")

        arquivos = ["anexo1.pdf", "anexo2.pdf"]
        compactar_arquivos(arquivos, "anexosCompactados")
        excluir_arquivos(arquivos)

    except Exception as e:
        print(f"Erro durante a execução: {e}")
    finally:
        navegador.quit()  # fecha navegador

if __name__ == '__main__':
    main()