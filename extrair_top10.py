import requests
from bs4 import BeautifulSoup

conteudo = None
URL = 'https://www.imdb.com/chart/top/'

try:
    respsota = requests.get(URL)
    respsota.raise_for_status()

except HTTPError as exc:
    print(exc.response)

else:
    conteudo = resposta.text

    with open(file='top10.html', mode='w', encoding='utf8') as arquivo:
        arquivo.write(conteudo)

    pagina = BeautifulSoup(open(file='top10.html', mode='r', encoding='utf8'), 'html.parser')
    texto = pagina.get_text()

    print(texto)