from crawl_website import crawl_website
from bs4 import BeautifulSoup
import csv

conteudo = None
URL = 'https://github.com/trending'
headers = {'User-Agent': 'Mozilla/5'}

conteudo = crawl_website(URL, headers=headers)

with open(file='github.html', mode='w', encoding='utf8') as arquivo:
    arquivo.write(conteudo)

pagina = BeautifulSoup(open('github.html', mode='r', encoding='utf-8'), 'html.parser')

conteudo_extraido = []

repositorios = pagina.find_all('article', class_='Box-row')

for i, repo in enumerate(pagina.find_all('article', class_='Box-row')[:10], start=1):
      # Extrair nome do projeto
      project_element = repo.find('h2', class_='h3 lh-condensed')
      project = project_element.get_text(strip=True).split(sep="/")[1] if project_element else None

      # Extrair os stars
      stars_element = repo.find('a', class_='Link Link--muted d-inline-block mr-3')
      stars = stars_element.text.strip() if stars_element else None

      # Extrair os stars_today
      stars_today_element = repo.find('span', class_='d-inline-block float-sm-right')
      stars_today = stars_today_element.text.strip().split()[0] if stars_today_element else None

      # Extrair forks
      forks_element = repo.find('a', class_='Link Link--muted d-inline-block mr-3', text=lambda text: text and 'Forks' in text)  # Filter by text
      forks = forks_element.text.strip() if forks_element else None

      # Extrair language
      language_element = repo.find('span', class_='d-inline-block ml-0 mr-3')
      language = language_element.text.strip() if language_element else None

      # Juntar todos os elementos
      conteudo_extraido.append([i, project, stars, stars_today, forks, language])

for dados in conteudo_extraido:
    print(dados)

i = []
project = []
stars = []
stars_today = []
forks = []
language = []

for linha in conteudo_extraido:
    i.append(linha[0])
    project.append(linha[1])
    stars.append(linha[2])
    stars_today.append(linha[3])
    forks.append(linha[3])
    language.append(linha[5])

with open(file='./github.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=';')
    escritor_csv.writerow(['ranking', 'project', 'language', 'stars', 'stars_today', 'forks'])
    dados = zip(i, project, language, stars, stars_today, forks)
    escritor_csv.writerows(dados)
