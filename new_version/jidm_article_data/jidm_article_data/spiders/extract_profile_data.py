# # -*- coding: utf-8 -*-
# import scrapy
# from bs4 import BeautifulSoup
# import requests
# from time import sleep
# from shortuuid import uuid


# class ExtractProfileDataSpider(scrapy.Spider):
#     name = 'extract_profile_data'
#     allowed_domains = ['https://dblp.uni-trier.de/']

#     list_names = ['Alex M. G. de Almeida', 'Alex Sandro Romeo de Souza Poletto', 'Alexander Vinson', 'André Dias Bastos', 'Angelo Frozza', 'Augusto B. Corrêa', 'Bruno Agostinho', 'Carlos Eduardo Pires', 'Caroline Tomasini', 'Cassio Prazeres', 'César Feijó Nadvorny', 'Cleto May', 'Cristian Tristão', 'Cristiano Politowski', 'Cristina Paludo Santos', 'Danilo S. da Cunha', 'Débora C. Nazário', 'Deise Saccol', 'Dinei A. Rockenbach', 'Douglas Dyllon J. de Macedo', 'Douglas Negrini', 'Edécio Iepsen', 'Edimar Manica', 'Edson Murakami', 'Elisa Mannes', 'Erick Lopes', 'Eugênio de Oliveira Simonetto', 'Fábio Pasquali', 'Felipe Victolla Silveira', 'Flávio R. Bayer', 'Frantchesco Cecchin', 'Geomar Schreiner',
#                   'Giancarlo Lucca', 'Glauber da Silva', 'Gustavo R. Forgiarini', 'Jeferson Kasper', 'Joaquim Assunção', 'José Guilherme C. de Souza', 'Juarez A. P. Sacenti', 'Juliana Bonato dos Santos', 'Juliano Augusto Carreira', 'Khaue Rodrigues', 'Larissa Lautert', 'Luis Fernando Milano Oliveira', 'Manuele Ferreira', 'Marcelo Telles', 'Mariusa Warpechowski', 'Miriam Colpo', 'Nádia Kozievitch', 'Rafael F. Machado', 'Raqueline Penteado', 'Renata Galante', 'Renato Deggau', 'Renato Fileto', 'Roberto Walter', 'Ronan Knob', 'Sérgio Mergen', 'Taisa C. Novello', 'Vania Elisabete Schneider', 'Vinicius F. Garcia', 'Vitor Hugo Bezerra', 'William Marx', 'Willian Ventura Koerich', 'Yuri Bichibichi']

#     # start_urls = ['https://dblp.org/pid/194/6129',
#     #               'https://dblp.org/pid/38/2915']

#     start_urls = ['https://dblp.org/pid/194/6129', 'https://dblp.org/pid/38/2915', 'https://dblp.org/pid/80/288', 'https://dblp.org/pid/29/5210', 'https://dblp.org/pid/77/3587', 'https://dblp.org/pid/194/6171', 'https://dblp.org/pid/232/5612', 'https://dblp.org/pid/59/4336', 'https://dblp.org/pid/139/3262', 'https://dblp.org/pid/06/710', 'https://dblp.org/pid/35/559', 'https://dblp.org/pid/153/4206', 'https://dblp.org/pid/36/7970', 'https://dblp.org/pid/180/3296', 'https://dblp.org/pid/54/5917', 'https://dblp.org/pid/126/2232', 'https://dblp.org/pid/135/0769', 'https://dblp.org/pid/b/DeisedeBrumSaccol', 'https://dblp.org/pid/246/0565', 'https://dblp.org/pid/02/3971', 'https://dblp.org/pid/119/0130', 'https://dblp.org/pid/193/4580', 'https://dblp.org/pid/84/8654', 'https://dblp.org/pid/178/4332', 'https://dblp.org/pid/85/8933', 'https://dblp.org/pid/184/5785', 'https://dblp.org/pid/69/10064', 'https://dblp.org/pid/157/0540', 'https://dblp.org/pid/82/87', 'https://dblp.org/pid/239/2608', 'https://dblp.org/pid/68/8419', 'https://dblp.org/pid/178/2074',
#                   'https://dblp.org/pid/116/8054', 'https://dblp.org/pid/117/5566', 'https://dblp.org/pid/41/4544', 'https://dblp.org/pid/120/1498', 'https://dblp.org/pid/133/6685', 'https://dblp.org/pid/66/1087', 'https://dblp.org/pid/153/4205', 'https://dblp.org/pid/91/60', 'https://dblp.org/pid/91/10804', 'https://dblp.org/pid/01/3808', 'https://dblp.org/pid/136/1410', 'https://dblp.org/pid/204/4278', 'https://dblp.org/pid/148/4409', 'https://dblp.org/pid/241/6821', 'https://dblp.org/pid/77/3594', 'https://dblp.org/pid/181/6608', 'https://dblp.org/pid/20/8212', 'https://dblp.org/pid/266/3479', 'https://dblp.org/pid/121/2219', 'https://dblp.org/pid/37/2418', 'https://dblp.org/pid/34/9384', 'https://dblp.org/pid/35/2350', 'https://dblp.org/pid/225/0632', 'https://dblp.org/pid/259/0491', 'https://dblp.org/pid/38/1094', 'https://dblp.org/pid/82/4205', 'https://dblp.org/pid/269/7852', 'https://dblp.org/pid/224/6851', 'https://dblp.org/pid/248/0124', 'https://dblp.org/pid/74/6623', 'https://dblp.org/pid/181/6587', 'https://dblp.org/pid/225/1836']

#     idx = 0

#     def parse(self, response):
#         years = self.get_years(self.start_urls[self.idx] + '.xml')

#         data = []

#         for publishe_raw, publishe_type, year in zip(response.css('li cite'), response.css('li div.box img::attr(title)').extract(), years):
#             ordem = 0
#             for i, author in enumerate(publishe_raw.css('span')):
#                 if 'this-person' in author.extract():
#                     ordem = (i+1)//2 + 1
#                     break

#             publishe_name = publishe_raw.css(
#                 'span.title::text').extract_first()
#             data.append({
#                 'id': uuid(),
#                 'titulo': publishe_name,
#                 'fonte': 'dblp',
#                 'ordem': ordem,
#                 'ano': year,
#                 'tipo': publishe_type
#             })

#         yield {
#             'nome': self.list_names[self.idx],
#             'artigos': data
#         }
#         self.idx += 1

#         if self.idx % 50 == 0:
#             sleep(180)

#     def get_years(self, url):
#         tmp = requests.get(url).text
#         years = [self.filter_year(y)
#                  for y in BeautifulSoup(tmp).findAll('year')]
#         return years

#     def filter_year(self, year):
#         return str(year).replace('<year>', '').replace('</year>', '')
