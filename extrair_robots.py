import re
from bs4 import BeautifulSoup
from crawl_website import crawl_website

conteudo = None
URL = 'https://www.imdb.com/robots.txt'
headers = {'User-Agent': 'Mozilla/5'}

conteudo = crawl_website(URL, headers=headers)

# Salvar a resposta no .html
with open(file='imdb_robo.html', mode='w', encoding='utf8') as arquivo:
    arquivo.write(conteudo)

# Parsear para transformar em .txt
pagina = BeautifulSoup(open('imdb_robo.html', mode='r'), 'html.parser')
texto = pagina.get_text()

if re.findall('top', texto, re.IGNORECASE) or re.findall('chart', texto, re.IGNORECASE):
    print(True)
else:
    print(False)

