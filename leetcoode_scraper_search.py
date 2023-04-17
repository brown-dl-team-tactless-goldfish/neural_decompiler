import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

SLEEP_TIME = 2

r = requests.get('https://leetcode.com/problemset/all/?page=1')
soup = BeautifulSoup(r.content, 'html.parser')

problem_list = soup.find_all('div', {'class': 'truncate'})
solution_list = []

df = pd.DataFrame()

for question in problem_list:
    problem_link = question.find('a', href=True).get('href')
    solution_list.append('https://leetcode.com' + problem_link + 'solutions/?languageTags=c')

for solution_link in solution_list:

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)
    driver.get(solution_link)
    time.sleep(SLEEP_TIME)
    search_bar = driver.find_element(By.XPATH, "//input[@type='text']").send_keys('C')
    time.sleep(5)
    sub_soup = BeautifulSoup(driver.page_source,'lxml')

    discussion_list = []

    for discussion in sub_soup.find_all('div', {'class': 'overflow-hidden text-ellipsis'}):
        discussion_list.append('https://leetcode.com' + str(discussion).partition('href="')[2].partition('"')[0])

    question_list = []
    link_list = []
    code_list = []

    for i, discussion in enumerate(discussion_list):
        question = discussion.partition('https://leetcode.com/problems/')[2].partition('/solutions/')[0]
        driver.get(discussion)
        time.sleep(SLEEP_TIME)
        sub_sub_soup = BeautifulSoup(driver.page_source,'lxml')
        time.sleep(SLEEP_TIME)

        text_list = []
        if sub_sub_soup.find('body').find('div', {'id': '__next'}).find('div', class_='break-words').find('div', class_='mb-6 rounded-lg px-3 py-2.5 font-menlo text-sm bg-fill-3 dark:bg-dark-fill-3'):
            for code in sub_sub_soup.find('body').find('div', {'id': '__next'}).find('div', class_='break-words').find_all('div', class_='mb-6 rounded-lg px-3 py-2.5 font-menlo text-sm bg-fill-3 dark:bg-dark-fill-3'):
                with open(question + '-' + str(i) + '.txt', 'w') as f:
                    f.write(code.text)