# Teste de Web Scraping

## Descrição
Este script automatiza o processo de navegação, download e manipulação de arquivos PDF a partir de uma URL específica. Ele utiliza Selenium para interagir com páginas web e Requests para baixar os PDFs. Após o download, os arquivos são compactados em um arquivo `.zip` e, posteriormente, excluídos da máquina local.

## Funcionalidades
1. Inicialização de um navegador headless (sem interface gráfica).
2. Navegação até elementos específicos em uma página para capturar URLs.
3. Download de arquivos PDF.
4. Compactação dos PDFs em um único arquivo `.zip`.
5. Exclusão dos arquivos PDF originais após a compactação.

## Pré-requisitos
Certifique-se de ter o **Python 3.7+** instalado em seu sistema e instalar as bibliotecas necessárias:

```bash
pip install -r requirements.txt