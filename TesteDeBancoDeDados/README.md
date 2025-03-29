# Teste de Banco de Dados

## Descrição
Este projeto automatiza o processamento de dados financeiros e cadastrais de operadoras de saúde, bem como a carga dessas informações em um banco de dados MySQL para análises mais avançadas. O código Python manipula e ajusta os dados em arquivos CSV, enquanto as queries SQL configuram o banco de dados, criam tabelas e carregam os dados necessários.

## Funcionalidades

### Código Python
1. **Manipulação de Datas**:
   - Ajusta o formato das datas de `dd/mm/yyyy` para `yyyy-mm-dd`.

2. **Conversão de Dados Financeiros**:
   - Transforma valores financeiros no formato brasileiro (com vírgula como separador decimal) para o formato numérico padrão (`float`).

3. **Manipulação de Arquivos**:
   - Salva os arquivos corrigidos em uma pasta designada.
   - Remove arquivos temporários criados durante o processamento.

4. **Execução do Fluxo Principal**:
   - Processa múltiplos arquivos trimestrais de demonstrações contábeis das operadoras de saúde.

### Queries SQL
1. **Estrutura do Banco de Dados**:
   - Criação do banco de dados `dadosfinanceiros`.
   - Configuração das tabelas `operadoras_saude` e `demonstracoes_contabeis` com chaves primárias e estrangeiras.

2. **Carga de Dados**:
   - Importa dados corrigidos de arquivos CSV para as tabelas do banco.

3. **Consultas de Análise**:
   - Identifica as 10 operadoras com maiores despesas em uma categoria específica no último trimestre e no último ano.

## Pré-requisitos
Certifique-se de ter o **Python 3.7+** e instale as dependências necessárias com:

```bash
pip install -r requirements.txt