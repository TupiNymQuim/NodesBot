import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from flask import Flask, request

app = Flask(__name__)

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

def getTotalStake(bs):
    rs = bs.findAll('p', {'class':'chakra-text css-9hpz1u'})
    return (rs[0].get_text())

def getSaturation(bs):
    rs = bs.findAll('p', {'class':'chakra-text css-lbk3c9'})
    return (rs[0].get_text())

def getBS(html):
    driver.get(html)
    time.sleep(0.3)
    html = driver.page_source
    bs = BeautifulSoup(html, 'html.parser')
    info = []
    key = ['title', 'hourscore', 'routingscore', 'totalstake', 'saturation']
    info.append(getTitle(bs))
    info.append(getHourScore(bs))
    info.append(getRoutingScore(bs))
    info.append(getTotalStake(bs))
    info.append(getSaturation(bs))
    ret = dict(zip(key, info))
    return (ret)

@app.route("/tupi1")
def tupi1():
    info = getBS("https://mixnet.explorers.guru/mixnode/7PvubVkboJQm881PxAJR6oBkMB6f8R1Au55tQjnmTasr")
    print(info)
    return info

@app.route("/tupi2")
def tupi2():
    info = getBS("https://mixnet.explorers.guru/mixnode/7r4gtQGLbLZfJ9m1b5LmBksxLbvAzfRy6fqzeLAdwwY6")
    print(info)
    return info


@app.route("/tupi3")
def tupi3():
    info = getBS("https://mixnet.explorers.guru/mixnode/DtQCygzXZsPT3D8ioqESBiWdCT2S1n11vJZWHKcMBy8t")
    print(info)
    return info


@app.route("/tupi4")
def tupi4():
    info = getBS("https://mixnet.explorers.guru/mixnode/7hhM8iyqXkkK7rg3gwoL2nw9wijmb5nMXH8MBtfUaban")
    print(info)
    return info

@app.route("/tupi5")
def tupi5():
    info = getBS("https://mixnet.explorers.guru/mixnode/4PP6FnME2EF9hgu4Teo4BJ3q4iNfGmuAzC4gFHFY2jnK")
    print(info)
    return info

@app.route("/tupi6")
def tupi6():
    info = getBS("https://mixnet.explorers.guru/mixnode/EfX72q3f5o1rTRjEJQASyWwPnRChLrBH77xL2EUgUtBX")
    print(info)
    return info

if __name__ == "__main__":
    app.run(debug=True)
