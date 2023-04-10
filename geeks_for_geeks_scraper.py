import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get('https://www.geeksforgeeks.org/c-programming-examples/')
soup = BeautifulSoup(r.content, 'html.parser')
code_list = []

url_list = soup.find_all('a', href=True)
for i in range(len(url_list)):
    url_list[i] = url_list[i].get('href')

url_list = [x for x in url_list if 'c-program-to' in x]

for url in url_list:
    r = requests.get(url)
    sub_soup = BeautifulSoup(r.content, 'html.parser')
    table_text = sub_soup.find('table').get_text()
    code_list.append(table_text)
    print(url)

df = pd.DataFrame()
df['code'] = code_list
df.to_csv('geeks_for_geeks_output.csv')