from selenium import webdriver
import time
import datetime
import shutil
from config import login, password
import pickle
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from random import randint
import pyautogui
# options
options = webdriver.ChromeOptions()

# user-agent
options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# for ChromeDriver version 79.0.3945.16 or over
options.add_argument("--disable-blink-features=AutomationControlled")

# headless mode

LOGIN_URL = 'https://id.mcfr.ua/Logon'
BASE_URL = 'https://1k.expertus.ua/'
PATH = "D:\develop\pypr\selenium_scraper\chromedriver.exe"
driver = webdriver.Chrome(
    PATH,
    options=options
)

try:
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
    time.sleep(3)
    print('authorized')
    names = [
        # '1',
        # 'штатний_розпис',
        # 'звільнення',
        # 'переведення',
        # 'посада',
        # 'Номенклатура справ',
        # 'Прийняття на роботу',
        # 'Перевірка з праці',
        # 'Посадова інструкція',
        # 'особова_картка',


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
        # 'оплата_праці',
        # 'Листок непрацездатності',
        # 'журнал',
        # 'трудова книжка',
        # 'заробітна плата',
        # 'колективний договір',
        # 'Атестація працівників',
        'догляд за дитиною',
    ]
    for file_name in names:
        try:
            try:
                os.makedirs(rf'D:\поиски\website\otpusk\{file_name}')
            except Exception:
                pass
            os.chdir(r'D:\develop\pypr\selenium_scraper')
            with open(f'{file_name}_hrefs.txt', 'r') as f:
                links = f.readlines()
                for link in links:
                    driver.get(link)
                    try:
                        driver.find_element_by_css_selector(
                            '#greyboard > div > div > div.doc-access__actions > button').click()
                        time.sleep(2)
                        driver.refresh()
                    except:
                        driver.refresh()
                        time.sleep(2)
                    try:
                        driver.find_element_by_css_selector(
                            "#main-left > div > div > section > div > div > div.doc.doc-card > div > div > div.doc-card__menu.no-print > div > ul > li:nth-child(4) > a > svg > use").click()
                        time.sleep(4)
                        os.chdir(r'C:\Users\georg\Downloads')
                        for file_ in os.listdir():
                            base_dir_path = os.path.abspath(file_)
                            file_end = file_
                            file_end = file_end.split('.')[-1]
                            if file_end not in ('doc', 'docx', 'pdf') or file_end == 'tmp' or file_end == 'crdownload':
                                os.unlink(base_dir_path)
                            else:
                                try:
                                    shutil.move(
                                        base_dir_path, rf'D:\поиски\website\otpusk\{file_name}')
                                except Exception:
                                    os.unlink(base_dir_path)

                        continue
                    except Exception as e:
                        print(e)
                    try:
                        driver.find_element_by_css_selector(
                            "#document-header > div > div.doc-header__in > div > div:nth-child(3) > ul > li:nth-child(1) > a").click()
                        time.sleep(4)
                        os.chdir(r'C:\Users\georg\Downloads')
                        for file_ in os.listdir():
                            base_dir_path = os.path.abspath(file_)
                            file_end = file_
                            file_end = file_end.split('.')[-1]
                            if file_end not in ('doc', 'docx', 'pdf') or file_end == 'tmp' or file_end == 'crdownload':
                                os.unlink(base_dir_path)
                            else:
                                try:
                                    shutil.move(
                                        base_dir_path, rf'D:\поиски\website\otpusk\{file_name}')
                                except Exception:
                                    os.unlink(base_dir_path)
                        continue
                    except Exception as e:
                        print(e)

                    try:
                        driver.find_element_by_css_selector(
                            "#document-header > div > div.doc-header__in > div > div.doc-header__item.doc-menu > ul > li:nth-child(4) > a").click()
                        time.sleep(4)
                        os.chdir(r'C:\Users\georg\Downloads')
                        for file_ in os.listdir():
                            base_dir_path = os.path.abspath(file_)
                            file_end = file_
                            file_end = file_end.split('.')[-1]
                            if file_end not in ('doc', 'docx', 'pdf') or file_end == 'tmp' or file_end == 'crdownload':
                                os.unlink(base_dir_path)
                            else:
                                try:
                                    shutil.move(
                                        base_dir_path, rf'D:\поиски\website\otpusk\{file_name}')
                                except Exception:
                                    os.unlink(base_dir_path)
                        continue
                    except Exception as e:
                        print(e)
                        
        
            try:
                os.chdir(r'C:\Users\georg\Downloads')
                for file_ in os.listdir():
                    base_dir_path = os.path.abspath(file_)
                    try:
                        shutil.move(
                            base_dir_path, rf'D:\поиски\website\otpusk\{file_name}')
                    except Exception:
                        os.unlink(base_dir_path)

            except Exception as e:
                os.chdir(r'D:\develop\pypr\selenium_scraper')
                with open('log.txt', 'a') as f:
                    f.write(f'Breaked on moveall rest files on {file_name} on excpetion \n \t\t {e}\n')    
                print(e)
        except Exception as e:
            os.chdir(r'D:\develop\pypr\selenium_scraper')
            with open('log.txt', 'a') as f:
                f.write(f'Breaked on loop on {file_name} on excpetion \n \t\t {e}\n')    
            continue
except Exception as e:
    print(e)
finally:
    driver.close()
