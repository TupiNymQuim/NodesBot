import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

options = Options()
# options.add_argument("start-maximized")
options.add_argument('--headless=new')
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument('--disable-3d-apis')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox-')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)


def getTitle(bs):
    rs = bs.findAll('p', {'class':'chakra-text css-1jijfcn'})
    return (rs[0].get_text())

def getRoutingScore(bs):
    rs = bs.findAll('p', {'class':'chakra-text css-2ar9as'})
    return (rs[0].get_text())

def getHourScore(bs):
    rs = bs.findAll('p', {'class':'chakra-text css-1fe1nli'})
    return (rs[0].get_text())

def getBS(html):
    driver.get(html)
    time.sleep(3)
    html = driver.page_source
    driver.close()
    bs = BeautifulSoup(html, 'html.parser')
    return (bs)

