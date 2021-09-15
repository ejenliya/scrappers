# from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from fake_useragent import UserAgent
import pyautogui

user_agents = [

]

useragent = UserAgent()
options = webdriver.ChromeOptions()

#disable browser

# options.add_argument(f"user-agent={useragent.Chrome}")
options.add_argument(
    f"user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
PATH = "D:\develop\pypr\selenium_scraper\chromedriver.exe"
driver = webdriver.Chrome(
    PATH,
    options=options
    )
url = 'https://www.freepik.com/profile/login'
try:
    driver.get(url)
    facebook_btn = driver.find_element_by_id('login-facebook').click()
    # time.sleep(15)\
    time.sleep(4)
    # pyautogui.press('tab')
    # pyautogui.press('tab')
    # pyautogui.write('detibudushego@icn.od.ua')
    # pyautogui.press('tab')
    # pyautogui.write('george_0912')
    # pyautogui.press('tab')
    # pyautogui.press('enter')

    driver.refresh()
    # driver.get_screenshot_as_file('1.png')
    # driver.save_screenshot("2.png")
except Exception as ex:
    print(ex)
finally:
    ...
    # driver.close()
    # driver.quit()


# from selenium import webdriver
# import time


# # options
# options = webdriver.ChromeOptions()

# # user-agent
# options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")


# # for ChromeDriver version 79.0.3945.16 or over
# options.add_argument("--disable-blink-features=AutomationControlled")
# # options.headless = True
# driver = webdriver.Chrome(
#     executable_path="D:\develop\pypr\selenium_scraper\chromedriver.exe",
#     options=options
# )

# try:
#     driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
#     time.sleep(10)
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()