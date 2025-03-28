-- 1: Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
USE dadosfinanceiros;
SELECT 
    o.REGISTRO_ANS,
    o.NOME_FANTASIA,
    SUM(d.VL_SALDO_FINAL - d.VL_SALDO_INICIAL) AS TOTAL_DESPESA
FROM 
    demonstracoes_contabeis d
JOIN 
    operadoras_saude o ON d.REG_ANS = o.REGISTRO_ANS
WHERE 
    d.DESCRICAO = "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR "
    and d.DATA = "2024-10-01"
GROUP BY 
    o.REGISTRO_ANS, o.NOME_FANTASIA
ORDER BY 
    TOTAL_DESPESA DESC
LIMIT 10;

-- 2: Quais as 10 operadoras com maiores despesas nessa categoria no último ano?
USE dadosfinanceiros;
SELECT 
    o.REGISTRO_ANS,
    o.NOME_FANTASIA,
    SUM(d.VL_SALDO_FINAL - d.VL_SALDO_INICIAL) AS TOTAL_DESPESA
FROM 
    demonstracoes_contabeis d
JOIN 
    operadoras_saude o ON d.REG_ANS = o.REGISTRO_ANS
WHERE 
    d.DESCRICAO = "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR "
    AND (
        d.DATA = "2024-10-01" OR 
        d.DATA = "2024-07-01" OR 
        d.DATA = "2024-04-01" OR 
        d.DATA = "2024-01-01"
    )
GROUP BY 
    o.REGISTRO_ANS, o.NOME_FANTASIA
ORDER BY 
    TOTAL_DESPESA DESC
LIMIT 10;