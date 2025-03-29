# Teste de Transformação de Dados

## Descrição
Este script automatiza a extração, manipulação e compactação de dados de um arquivo PDF contido em um arquivo `.zip`. Ele utiliza a biblioteca Tabula para extrair tabelas dos PDFs e pandas para manipular e salvar os dados como arquivos CSV. Além disso, ele realiza compactação e exclusão de arquivos de forma automatizada.

## Funcionalidades
1. **Extração de arquivos ZIP**: Identifica e extrai um arquivo específico de um arquivo `.zip`.
2. **Leitura de PDFs**: Extrai tabelas de um arquivo PDF utilizando a biblioteca Tabula.
3. **Manipulação de dados**: Limpa e organiza os dados das tabelas extraídas.
4. **Exportação para CSV**: Combina as tabelas processadas e as salva em formato `.csv`.
5. **Compactação de CSVs**: Compacta arquivos CSV em um novo `.zip`.
6. **Exclusão de arquivos temporários**: Remove arquivos gerados localmente após o processamento.

## Pré-requisitos
Certifique-se de ter o **Python 3.7+** instalado em seu sistema e instalar as bibliotecas necessárias:

```bash
pip install -r requirements.txt