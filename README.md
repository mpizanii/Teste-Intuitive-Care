# Teste-Intuitive-Care

Este repositório contém a implementação dos testes solicitados para o processo de seleção.

## 1. Teste de Web Scraping

### Objetivo
Realizar web scraping no site da ANS para baixar e compactar arquivos PDF.

### Tarefas
- Acessar o site: [ANS - Atualização do Rol de Procedimentos](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos)
- Baixar os Anexos I e II em formato PDF.
- Compactar todos os anexos em um único arquivo ZIP.
- Tecnologia utilizada: Python.

---

## 2. Teste de Transformação dos Dados

### Objetivo
Extrair e transformar dados do PDF baixado.

### Tarefas
- Extrair os dados da tabela "Rol de Procedimentos e Eventos em Saúde" do Anexo I (todas as páginas).
- Salvar os dados extraídos em um arquivo CSV estruturado.
- Substituir as abreviações das colunas OD e AMB pelas descrições completas.
- Compactar o CSV em um arquivo denominado `Teste_Matheus_Pizani.zip`.
- Tecnologia utilizada: Python.

---

## 3. Teste de Banco de Dados

### Objetivo
Criar e estruturar tabelas para armazenar os dados das operadoras de planos de saúde.

### Tarefas
- Baixar os arquivos dos últimos 2 anos do repositório público:  
  [Demonstrativos Contábeis](https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/)
- Baixar os dados cadastrais das operadoras ativas da ANS no formato CSV:  
  [Operadoras Ativas](https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/)
- Criar queries para estruturar as tabelas do banco de dados.
- Elaborar queries para importar os arquivos preparados.
- Desenvolver consultas analíticas para:
  - Identificar as 10 operadoras com maiores despesas em "EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE MÉDICO-HOSPITALAR" no último trimestre.
  - Identificar as 10 operadoras com maiores despesas nessa categoria no último ano.
- Tecnologias utilizadas: Python e MySQL.

---

## 4. Teste de API

### Objetivo
Criar uma interface web interativa usando Vue.js conectada a um backend em Python.

### Tarefas
- Utilizar o [CSV](https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/) utilizado no item anterior como base de dados.
- Criar um servidor com uma rota que realize buscas textuais na lista de cadastros de operadoras.
- Retornar os registros mais relevantes para a busca.
- Elaborar uma coleção no Postman para demonstrar o funcionamento da API.
- Tecnologias utilizadas: Python(Django); Vue.js e Postman.