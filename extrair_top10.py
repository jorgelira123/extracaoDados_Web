import re
from bs4 import BeautifulSoup
from crawl_website import crawl_website
import csv

conteudo = None
URL = 'https://www.imdb.com/chart/top/'
headers = {'User-Agent': 'Mozilla/5'}

conteudo = crawl_website(URL, headers=headers)

# Salvar a resposta no .html
with open(file='top10.html', mode='w', encoding='utf8') as arquivo:
    arquivo.write(conteudo)

# Parsear para transformar em .txt
pagina = BeautifulSoup(open('top10.html', mode='r', encoding='utf-8'), 'html.parser')

conteudo_extraido = []

movies = pagina.find_all("li", class_="ipc-metadata-list-summary-item")

for coluna in movies[:10]:
    textos_coluna = coluna.get_text(";").strip().split(";")
    textos_coluna = textos_coluna[0].split(".") + textos_coluna[1:]
    conteudo_extraido.append(textos_coluna)

for filme in conteudo_extraido:
    print(filme)

ranking = []
titulo = []
ano = []
nota = []

for linha in conteudo_extraido:
    ranking.append(linha[0])
    titulo.append(linha[1].strip())
    ano.append(linha[2])
    nota.append(linha[5])

with open(file='./imdb.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=';')
    escritor_csv.writerow(['ranking', 'titulo', 'ano', 'nota'])
    dados = zip(ranking, titulo, ano, nota)
    escritor_csv.writerows(dados)
