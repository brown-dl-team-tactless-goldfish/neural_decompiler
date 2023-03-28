import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

SLEEP_TIME = 2

r = requests.get('https://leetcode.com/problemset/all/?page=1')
soup = BeautifulSoup(r.content, 'html.parser')

problem_list = soup.find_all('div', {'class': 'truncate'})
solution_list = []

for problem in problem_list:
    problem_link = problem.find('a', href=True).get('href')
    solution_list.append('https://leetcode.com' + problem_link + 'solutions/?languageTags=c')

driver = webdriver.Chrome()
driver.get(solution_list[0])
time.sleep(SLEEP_TIME)
driver.find_element(By.ID, 'headlessui-popover-button-:r2:').click()
time.sleep(SLEEP_TIME)
driver.find_element(By.XPATH, "//span[text()='C']").click()
sub_soup = BeautifulSoup(driver.page_source,'lxml')

discussion_list = []

for discussion in sub_soup.find_all('div', {'class': 'overflow-hidden text-ellipsis'}):
    discussion_list.append('https://leetcode.com' + str(discussion).partition('href="')[2].partition('"')[0])

for i, discussion in enumerate(discussion_list):
    driver.get(discussion)
    time.sleep(SLEEP_TIME)
    sub_sub_soup = BeautifulSoup(driver.page_source,'lxml')
    text = sub_sub_soup.find('body').text
    print(text)
