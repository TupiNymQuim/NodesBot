import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from flask import Flask, request

app = Flask(__name__)

options = Options()
options.add_argument('--headless=new')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox-')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

def getRoutingScore(bs):
    rs = bs.findAll('p', {'id':'avgUptime'})
    return (rs[0].get_text())

def getHourScore(bs):
    rs = bs.findAll('p', {'id':'nodePerformance'})
    return (rs[0].get_text())
    
def getTotalStake(bs):
    rs = bs.findAll('td', {'data-testid':'bond-total-amount'})
    return (rs[0].get_text())
    
def getSaturation(bs):
    rs = bs.findAll('p', {'id':'stake-saturation-progress-bar'})
    return (rs[0].get_text())
    
def getLocation(bs):
    rs = bs.findAll('th', {'data-testid':'Location-value'})
    return (rs[0].get_text())
    
def getBS(html):
    driver.get(html)
    time.sleep(0.2)
    html = driver.page_source
    bs = BeautifulSoup(html, 'html.parser')
    info = []
    info.append(getHourScore(bs))
    info.append(getRoutingScore(bs))
    info.append(getTotalStake(bs))
    info.append(getSaturation(bs))]
    info.append(getLocation(bs))
    return (ret)

@app.route("/tupi1")
def tupi1():
    info = getBS("https://explorer.nymtech.net/network-components/mixnode/1356")
    key = ['title', 'hourscore', 'routingscore', 'totalstake', 'saturation', 'location']
    info.insert(0, "TupiNymQuim 1")
    ret = dict(zip(key, info))
    print(ret)
    return ret

@app.route("/tupi2")
def tupi2():
    info = getBS("https://explorer.nymtech.net/network-components/mixnode/1357")
    key = ['title', 'hourscore', 'routingscore', 'totalstake', 'saturation', 'location']
    info.insert(0, "TupiNymQuim 2")
    ret = dict(zip(key, info))
    print(ret)
    return ret


@app.route("/tupi3")
def tupi3():
    info = getBS("https://explorer.nymtech.net/network-components/mixnode/1359")
    key = ['title', 'hourscore', 'routingscore', 'totalstake', 'saturation', 'location']
    info.insert(0, "TupiNymQuim 3")
    ret = dict(zip(key, info))
    print(ret)
    return ret


@app.route("/tupi4")
def tupi4():
    info = getBS("https://explorer.nymtech.net/network-components/mixnode/1365")
    key = ['title', 'hourscore', 'routingscore', 'totalstake', 'saturation', 'location']
    info.insert(0, "TupiNymQuim 4")
    ret = dict(zip(key, info))
    print(ret)
    return ret

@app.route("/tupi5")
def tupi5():
    info = getBS("https://explorer.nymtech.net/network-components/mixnode/1362")
    key = ['title', 'hourscore', 'routingscore', 'totalstake', 'saturation', 'location']
    info.insert(0, "TupiNymQuim 5")
    ret = dict(zip(key, info))
    print(ret)
    return ret

@app.route("/tupi6")
def tupi6():
   info = getBS("https://explorer.nymtech.net/network-components/mixnode/1368")
   key = ['title', 'hourscore', 'routingscore', 'totalstake', 'saturation', 'location']
   info.insert(0, "TupiNymQuim 6")
   ret = dict(zip(key, info))
   print(ret)
   return ret

if __name__ == "__main__":
    app.run(debug=True)
