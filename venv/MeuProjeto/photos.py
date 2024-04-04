import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/photos')

try:
    print('=' * 100)
    print('| Requisição bem-sucedida! |'.center(100))
    print('-' * 100)
    
    dados = json.loads(response.text)
    for item in dados:
        print(f"ID: {item['id']}")
        print(f"   AlbumID: {item['albumId']}")
        print(f"   Título: {item['title']}")
        print(f"   URL: {item['url']}")
        print(f"   Thumbnail URL: {item['thumbnailUrl']}", end = '\n\n')
        print("*" * 100, end = '\n\n')
        
    print("=" * 100)
        
except TypeError:
    print('Erro de tipo')
    pass
except requests.exceptions.HTTPError as errh:
    print(f'Erro HTTP: {errh}')
except requests.exceptions.ConnectionError as errc:
    print(f'Erro de conexão: {errc}')
except requests.exceptions.Timeout as errt:
    print(f'Tempo de resposta excedido: {errt}')
except requests.exceptions.RequestException as err:
    print(f'Erro de aquisição: {err}')

if response.status_code == 200:
    print('=' * 100)
    print('| Programa finalizado com sucesso! |'.center(100))
    print('=' * 100)
