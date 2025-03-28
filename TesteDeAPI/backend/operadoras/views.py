import csv
from django.http import JsonResponse

def buscar_operadoras_csv(request):  
    try:  
        termo = request.GET.get('q', '').lower()

        resultados = []

        caminho_csv = 'operadoras/csv/operadoras.csv'

        with open(caminho_csv, 'r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo, delimiter=';')
            for linha in leitor:
                if 'Razao_Social' in linha and 'Nome_Fantasia' in linha:
                    if termo in linha['Razao_Social'].lower() or termo in linha['Nome_Fantasia'].lower():
                        resultados.append({
                            'registro_ans': linha.get('Registro_ANS', 'Não disponível'),  
                            'nome_fantasia': linha.get('Nome_Fantasia', 'Não disponível'),
                            'razao_social': linha.get('Razao_Social', 'Não disponível'),
                            'cidade': linha.get('Cidade', 'Não disponível'),
                            'UF': linha.get('UF', 'Não disponível'),
                        })

        return JsonResponse(resultados, safe=False)
    except FileNotFoundError:  
        return JsonResponse({'erro': f"Arquivo '{caminho_csv}' não encontrado."}, status=404)
    except Exception as e:  
        return JsonResponse({'erro': f"Erro ao processar o arquivo: {e}"}, status=500)