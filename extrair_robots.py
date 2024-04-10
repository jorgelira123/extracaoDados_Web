import re
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

conteudo = None
URL = 'https://www.imdb.com/robots.txt'

try:
    resposta = requests.get(URL)
    resposta.raise_for_status()

except HTTPError as exc:
    print(exc.response)

else:
    conteudo = resposta.text
    with open(file='imdb_robo.html', mode='w', encoding='utf8') as arquivo:
        arquivo.write(conteudo)

    pagina = BeautifulSoup(open('imdb_robo.html', mode='r'), 'html.parser')
    texto = pagina.get_text()

    if re.findall('top', texto, re.IGNORECASE) or re.findall('chart', texto, re.IGNORECASE):
        print(True)
    else:
        print(False)
