# Consumindo uma API e exibindo dados em Python

Este é um simples script Python que consome uma API e exibe os dados obtidos de forma organizada.

## Pré-requisitos

Antes de executar este script, certifique-se de ter o Python instalado em sua máquina.

Além disso, este script requer a biblioteca `requests` para fazer solicitações HTTP e a biblioteca `json` para manipular dados JSON. Você pode instalá-las usando o gerenciador de pacotes pip:

```
pip install requests
```

## Como usar

1. Clone este repositório ou baixe o arquivo `script.py`.
2. Abra um terminal ou prompt de comando.
3. Navegue até o diretório onde o arquivo `script.py` está localizado.
4. Execute o script digitando o seguinte comando:

```
python script.py
```

Isso irá executar o script e exibir os dados obtidos da API de forma organizada.

## Sobre o script

O script utiliza a biblioteca `requests` para fazer uma **solicitação GET** para a API [JSONPlaceholder](https://jsonplaceholder.typicode.com/). Se a solicitação for bem-sucedida (`status code 200`), ele processa os dados JSON retornados e exibe as informações de cada item em um loop que são exibidas de forma organizada.