import time
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import Flask, request
from waitress import serve

app = Flask(__name__)

def getInfo(bs, title="title"):
    total_stake = str(float(bs['pledge_amount']['amount'])/1000000 + float(bs['total_delegation']['amount'])/1000000)
    avg_uptime = str(bs['avg_uptime'])
    node_performance = str(float(bs['node_performance']['most_recent']) * 100)
    location = bs['location']['country_name']
    key = ['title', 'avg_uptime', 'node_performance', 'total_stake', 'location']
    res = []
    res.insert(0, title)
    res.insert(1, avg_uptime)
    res.insert(2, node_performance)
    res.insert(3, total_stake)
    res.insert(4, location)
    ret = dict(zip(key, res))
    return  ret
    

@app.route("/tupi1")
def tupi1():
    info = urlopen("https://explorer.nymtech.net/api/v1/mix-node/1356")
    bs = json.loads(str(BeautifulSoup(info, 'html.parser')))
    title = 'TupiNymQuim 1'
    res = getInfo(bs, title)
    return res

@app.route("/tupi2")
def tupi2():
    info = urlopen("https://explorer.nymtech.net/api/v1/mix-node/1357")
    bs = json.loads(str(BeautifulSoup(info, 'html.parser')))
    title = 'TupiNymQuim 2'
    res = getInfo(bs, title)
    return res


@app.route("/tupi3")
def tupi3():
    info = urlopen("https://explorer.nymtech.net/api/v1/mix-node/1359")
    bs = json.loads(str(BeautifulSoup(info, 'html.parser')))
    title = 'TupiNymQuim 3'
    res = getInfo(bs, title)
    return res


@app.route("/tupi4")
def tupi4():
    info = urlopen("https://explorer.nymtech.net/api/v1/mix-node/1365")
    bs = json.loads(str(BeautifulSoup(info, 'html.parser')))
    title = 'TupiNymQuim 4'
    res = getInfo(bs, title)
    return  res

@app.route("/tupi5")
def tupi5():
    info = urlopen("https://explorer.nymtech.net/api/v1/mix-node/1362")
    bs = json.loads(str(BeautifulSoup(info, 'html.parser')))
    title = 'TupiNymQuim 5'
    res = getInfo(bs, title)
    return res


@app.route("/tupi6")
def tupi6():
   info = urlopen("https://explorer.nymtech.net/api/v1/mix-node/1368")
   bs = json.loads(str(BeautifulSoup(info, 'html.parser')))
   title = 'TupiNymQuim 6'
   res = getInfo(bs, title)
   return res

@app.route("/mixnodes/<nodeid>")
def mixnode(nodeid):
    info = urlopen("https://explorer.nymtech.net/api/v1/mix-node/"+ nodeid)
    bs = json.loads(str(BeautifulSoup(info, 'html.parser')))
    res = getInfo(bs)
    return res


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
