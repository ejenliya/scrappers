from config import login, password
from selenium import webdriver
import os
import shutil
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from fake_useragent import UserAgent
import pickle
import threading
from pathlib import Path
from time import sleep
from watchdog.observers import Observer
from EventHandler import EventHandler
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui

LOGIN_URL = 'https://id.mcfr.ua/Logon'
BASE_URL = 'https://1k.expertus.ua/'

useragent = UserAgent()
options = webdriver.ChromeOptions()

# options.add_argument(f"user-agent={useragent.Chrome}")
options.add_argument(
    f"user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument('--proxy-server=138.128.91.65:0000')

tags = [
    # 'звільнення',
    # 'переведення',
    # 'посада',
    # 'штатний розпис',
    # 'оплата праці',
    # 'особова картка',
    # 'Номенклатура справ',
    # 'Прийняття на роботу',
    # 'Перевірка з праці',
    # 'Посадова інструкція',
    # 'Облік робочого часу',
    # 'Вихідні дні',
    # 'Робочий час',
    # 'Неповний робочий час',
    # 'Накази',
    # 'ФОП',
    # 'Трудовий договір',
    # 'Положення про оплату праці',
    # 'Правила внутрішнього трудового розпорядку',
    # 'Графік відпусток',
    # 'Порушення',
    # 'Штрафи',
    # 'Колективний договір',
    # 'Карантин',
    # 'Дистанційна робота',
    'Листок непрацездатності',
    'журнал',
    'трудова книжка',
    'заробітна плата',
    'колективний договір',
    'Атестація працівників',
    'догляд за дитиною',

]


PATH = "D:\develop\pypr\selenium_scraper\chromedriver.exe"
driver = webdriver.Chrome(
    PATH,
    options=options
)
watch_path = Path(r'C:\Users\georg\Downloads')
destination_root = Path(r'D:\поиски\website')
event_handler = EventHandler(
    watch_path=watch_path, destination_root=destination_root, name=tags[0])


def watch():

    observer = Observer()
    observer.schedule(event_handler, f'{watch_path}', recursive=True)
    observer.start()

    try:
        while True:
            sleep(10000)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def authorize():
    driver.get(LOGIN_URL)

    email_input = driver.find_element_by_id('rx-user-field')
    email_input.clear()
    email_input.send_keys(login)
    password_input = driver.find_element_by_id('rx-pass-field')
    password_input.clear()
    password_input.send_keys(password)
    driver.find_element_by_id('rx-form-submit').click()
    pickle.dump(driver.get_cookies(), open(f"{login}_cookies", "wb"))
    time.sleep(3)
    driver.get(BASE_URL)
    time.sleep(2)
    driver.maximize_window()
    try:
        driver.find_element_by_css_selector(
            'body > div.subscription-popup.no-print > div.subscription-popup__close').click()
    except:
        pass


def search_by_keyword(keyword):
    driver.refresh()
    print(f'Now-> {keyword}')
    
    search_bar = driver.find_element_by_id('search-text')
    for  i in range(100):
        search_bar.send_keys(Keys.BACK_SPACE)
    search_bar.clear()
    search_bar.clear()
    search_bar.clear()
    search_bar.send_keys(keyword)
    search_bar.send_keys(Keys.ENTER)

    time.sleep(3)
    
    # driver.refresh()
    time.sleep(1)
    for i in range(100):
        print(f'Iteration -> {i}')
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    items = driver.find_elements_by_css_selector(
        'div.sc-fznxsB.fvMaWY > span > a')
    hrefs = [item.get_attribute('href') for item in items]
    with open(f'{keyword}_hrefs.txt', 'w') as f:
        for href in hrefs:
            f.write(href + '\n')


def download_from_links():
    with open('hrefs.txt', 'r') as f:
        hrefs = f.readlines()

    for href in hrefs:
        driver.get(href)
        time.sleep(3)
        try:
            driver.find_element_by_css_selector(
                '#greyboard > div > div > div.doc-access__actions > button').click()
            time.sleep(2)
            driver.refresh()
        except:
            driver.refresh()
            time.sleep(2)

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#main-left > div > div > section > div > div > div.doc.doc-card > div > div > div.doc-card__menu.no-print > div > ul > li:nth-child(4) > a > svg > use"))).click()
        time.sleep(3)


def selenium_work():
    try:
        authorize()
        for tag in tags:
            search_by_keyword(tag)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
selenium_work()