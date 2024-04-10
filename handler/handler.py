import sys
sys.path.append('/root/NodesBot/')
import json
import utils.utils as utils
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
    

def getGateway(bshealth, bsscore, bsroles, bsexit, title):
    status = str(bshealth['status'])
    uptime = str(bshealth['uptime'])
    most_recent = str(bsscore['most_recent'])
    nr = str(bsroles['network_requester_enabled'])
    ip_router = str(bsroles['ip_packet_router_enabled'])
    exit = str(bsexit['enabled'])
    key = ['title', 'status', 'uptime', 'most_recent', 'network_requester_enabled', 'ip_packet_router_enabled', 'exit_policy']
    res = []
    res.insert(0, title)
    res.insert(1, status)
    res.insert(2, uptime)
    res.insert(3, most_recent)
    if (nr == "True"):
        res.insert(4, "✅")
    else:
        res.insert(4, "❌")
    if (ip_router == "True"):
        res.insert(5, "✅")
    else:
        res.insert(5, "❌")
    if (exit == "True"):
        res.insert(6, "✅")
    else:
        res.insert(6, "❌")
    ret = dict(zip(key, res))
    return ret

@app.route("/gateway1")
def gateway1():
    title = 'Gateway 1 - Australia'
    try:
        health = urlopen("http://gateway1.tupinymquim.com:8080/api/v1/health", timeout=0.4)
        roles = urlopen("http://gateway1.tupinymquim.com:8080/api/v1/roles", timeout=0.4)
        exit = urlopen("http://gateway1.tupinymquim.com:8080/api/v1/network-requester/exit-policy", timeout=0.4)
        score = urlopen("https://validator.nymtech.net/api/v1/status/gateway/5SHU62fW1L4xMBEXnfxU9Zz49U9tjQUiDmqEcggUYMNb/report", timeout=0.4)
    except:
        key = ['title', 'status', 'uptime', 'most_recent', 'network_requester_enabled', 'ip_packet_router_enabled', 'exit_policy']
        res = []
        res.insert(0, title)
        res.insert(1, "down")
        res.insert(2, "0")
        res.insert(3, "0")
        res.insert(4, "❌")
        res.insert(5, "❌")
        res.insert(6, "❌")
        ret = dict(zip(key, res))
        return ret
    bshealth = json.loads(str(BeautifulSoup(health, 'html.parser')))
    bsroles = json.loads(str(BeautifulSoup(roles, 'html.parser')))
    bsscore = json.loads(str(BeautifulSoup(score, 'html.parser')))
    bsexit = json.loads(str(BeautifulSoup(exit,'html.parser' )))
    res = getGateway(bshealth, bsscore, bsroles, bsexit, title)
    return  res
    
@app.route("/gateway2")
def gateway2():
    title = 'Gateway 2 - Espanha'
    try:
        health = urlopen("http://gateway2.tupinymquim.com:8080/api/v1/health", timeout=0.4)
        exit = urlopen("http://gateway2.tupinymquim.com:8080/api/v1/network-requester/exit-policy", timeout=0.4)
        roles = urlopen("http://gateway2.tupinymquim.com:8080/api/v1/roles", timeout=0.4)
        score = urlopen("https://validator.nymtech.net/api/v1/status/gateway/AG1jucgspds2xXJAftZHr7tqf3haPNjWLyRsn9NzfWje/report", timeout=0.4)
    except:
        key = ['title', 'status', 'uptime', 'most_recent', 'network_requester_enabled', 'ip_packet_router_enabled', 'exit_policy']
        res = []
        res.insert(0, title)
        res.insert(1, "down")
        res.insert(2, "0")
        res.insert(3, "0")
        res.insert(4, "❌")
        res.insert(5, "❌")
        res.insert(6, "❌")
        ret = dict(zip(key, res))
        return ret
    bshealth = json.loads(str(BeautifulSoup(health, 'html.parser')))
    bsroles = json.loads(str(BeautifulSoup(roles, 'html.parser')))
    bsscore = json.loads(str(BeautifulSoup(score, 'html.parser')))
    bsexit = json.loads(str(BeautifulSoup(exit,'html.parser' )))
    res = getGateway(bshealth, bsscore, bsroles, bsexit, title)
    return  res


@app.route("/gateway3")
def gateway3():
    title = 'Gateway 3 - Brasil'
    try:
        health = urlopen("http://gateway3.tupinymquim.com:8080/api/v1/health", timeout=0.4)
        exit = urlopen("http://gateway3.tupinymquim.com:8080/api/v1/network-requester/exit-policy", timeout=0.4)
        roles = urlopen("http://gateway3.tupinymquim.com:8080/api/v1/roles", timeout=0.4)
        score = urlopen("https://validator.nymtech.net/api/v1/status/gateway/49PcvZKw3UHa3w88xCKKCshFWz139mPMx7ZEX2Wg9jqk/report", timeout=0.4)
    except:
        key = ['title', 'status', 'uptime', 'most_recent', 'network_requester_enabled', 'ip_packet_router_enabled', 'exit_policy']
        res = []
        res.insert(0, title)
        res.insert(1, "down")
        res.insert(2, "0")
        res.insert(3, "0")
        res.insert(4, "❌")
        res.insert(5, "❌")
        res.insert(6, "❌")
        ret = dict(zip(key, res))
        return ret
    bshealth = json.loads(str(BeautifulSoup(health, 'html.parser')))
    bsroles = json.loads(str(BeautifulSoup(roles, 'html.parser')))
    bsscore = json.loads(str(BeautifulSoup(score, 'html.parser')))
    bsexit = json.loads(str(BeautifulSoup(exit,'html.parser' )))
    res = getGateway(bshealth, bsscore, bsroles, bsexit, title)
    return  res

@app.route("/gateway4")
def gateway4():
    title = 'Gateway 4 - Itália'
    try:
        health = urlopen("http://gateway4.tupinymquim.com:8080/api/v1/health", timeout=0.4)
        exit = urlopen("http://gateway4.tupinymquim.com:8080/api/v1/network-requester/exit-policy", timeout=0.4)
        roles = urlopen("http://gateway4.tupinymquim.com:8080/api/v1/roles", timeout=0.4)
        score = urlopen("https://validator.nymtech.net/api/v1/status/gateway/DgD7K1RHn7kMPC3ibg6HkJFkDqaFstxpEFHgronRdCqj/report", timeout=0.4)
    except:
        key = ['title', 'status', 'uptime', 'most_recent', 'network_requester_enabled', 'ip_packet_router_enabled', 'exit_policy']
        res = []
        res.insert(0, title)
        res.insert(1, "down")
        res.insert(2, "0")
        res.insert(3, "0")
        res.insert(4, "❌")
        res.insert(5, "❌")
        res.insert(6, "❌")
        ret = dict(zip(key, res))
        return ret
    bshealth = json.loads(str(BeautifulSoup(health, 'html.parser')))
    bsroles = json.loads(str(BeautifulSoup(roles, 'html.parser')))
    bsscore = json.loads(str(BeautifulSoup(score, 'html.parser')))
    bsexit = json.loads(str(BeautifulSoup(exit,'html.parser' )))
    res = getGateway(bshealth, bsscore, bsroles, bsexit, title)
    return  res

@app.route("/gateway5")
def gateway5():
    title = 'Gateway 5 - Noruega'
    try:
        health = urlopen("http://gateway5.tupinymquim.com:8080/api/v1/health", timeout=0.4)
        exit = urlopen("http://gateway5.tupinymquim.com:8080/api/v1/network-requester/exit-policy", timeout=0.4)
        roles = urlopen("http://gateway5.tupinymquim.com:8080/api/v1/roles", timeout=0.4)
        score = urlopen("https://validator.nymtech.net/api/v1/status/gateway/8R9CjJsfWbAmisHcarJYLrvTdkW1D4CLyy3iAY89j5QF/report", timeout=0.4)
    except:
        key = ['title', 'status', 'uptime', 'most_recent', 'network_requester_enabled', 'ip_packet_router_enabled', 'exit_policy']
        res = []
        res.insert(0, title)
        res.insert(1, "down")
        res.insert(2, "0")
        res.insert(3, "0")
        res.insert(4, "❌")
        res.insert(5, "❌")
        res.insert(6, "❌")
        ret = dict(zip(key, res))
        return ret
    bshealth = json.loads(str(BeautifulSoup(health, 'html.parser')))
    bsroles = json.loads(str(BeautifulSoup(roles, 'html.parser')))
    bsscore = json.loads(str(BeautifulSoup(score, 'html.parser')))
    bsexit = json.loads(str(BeautifulSoup(exit,'html.parser' )))
    res = getGateway(bshealth, bsscore, bsroles, bsexit, title)
    return  res

@app.route("/gateway6")
def gateway6():
    title = 'Gateway 6 - Singapura'
    try:
        health = urlopen("http://gateway6.tupinymquim.com:8080/api/v1/health", timeout=0.4)
        exit = urlopen("http://gateway6.tupinymquim.com:8080/api/v1/network-requester/exit-policy", timeout=0.4)
        roles = urlopen("http://gateway6.tupinymquim.com:8080/api/v1/roles", timeout=0.4)
        score = urlopen("https://validator.nymtech.net/api/v1/status/gateway/Eb15FTXQgnenwLmqdfCQNj6PmKjMszrmHhtXqKKRafMW/report", timeout=0.4)
    except:
        key = ['title', 'status', 'uptime', 'most_recent', 'network_requester_enabled', 'ip_packet_router_enabled', 'exit_policy']
        res = []
        res.insert(0, title)
        res.insert(1, "down")
        res.insert(2, "0")
        res.insert(3, "0")
        res.insert(4, "❌")
        res.insert(5, "❌")
        res.insert(6, "❌")
        ret = dict(zip(key, res))
        return ret
    bshealth = json.loads(str(BeautifulSoup(health, 'html.parser')))
    bsroles = json.loads(str(BeautifulSoup(roles, 'html.parser')))
    bsscore = json.loads(str(BeautifulSoup(score, 'html.parser')))
    bsexit = json.loads(str(BeautifulSoup(exit,'html.parser' )))
    res = getGateway(bshealth, bsscore, bsroles, bsexit, title)
    return  res

@app.route("/gateway7")
def gateway7():
    title = 'Gateway 7 - Bélgica'
    try:
        health = urlopen("http://gateway7.tupinymquim.com:8080/api/v1/health", timeout=0.4)
        exit = urlopen("http://gateway7.tupinymquim.com:8080/api/v1/network-requester/exit-policy", timeout=0.4)
        roles = urlopen("http://gateway7.tupinymquim.com:8080/api/v1/roles", timeout=0.4)
        score = urlopen("https://validator.nymtech.net/api/v1/status/gateway/5P8MmJTdmoS4rhV8VHArABkyPE3M9RMrZsiX3qYkJ6u/report", timeout=0.4)
    except:
        key = ['title', 'status', 'uptime', 'most_recent', 'network_requester_enabled', 'ip_packet_router_enabled', 'exit_policy']
        res = []
        res.insert(0, title)
        res.insert(1, "down")
        res.insert(2, "0")
        res.insert(3, "0")
        res.insert(4, "❌")
        res.insert(5, "❌")
        res.insert(6, "❌")
        ret = dict(zip(key, res))
        return ret
    bshealth = json.loads(str(BeautifulSoup(health, 'html.parser')))
    bsroles = json.loads(str(BeautifulSoup(roles, 'html.parser')))
    bsscore = json.loads(str(BeautifulSoup(score, 'html.parser')))
    bsexit = json.loads(str(BeautifulSoup(exit,'html.parser' )))
    res = getGateway(bshealth, bsscore, bsroles, bsexit, title)
    return  res

@app.route("/gateway8")
def gateway8():
    title = 'Gateway 8 - África do Sul'
    try:
        health = urlopen("http://gateway8.tupinymquim.com:8080/api/v1/health", timeout=0.4)
        exit = urlopen("http://gateway8.tupinymquim.com:8080/api/v1/network-requester/exit-policy", timeout=0.4)
        roles = urlopen("http://gateway8.tupinymquim.com:8080/api/v1/roles", timeout=0.4)
        score = urlopen("https://validator.nymtech.net/api/v1/status/gateway/FGQXnYX5JFEA71ZUUNU2JkrLYpbjraYthQvnTgVKvXVX/report", timeout=0.4)
    except:
        key = ['title', 'status', 'uptime', 'most_recent', 'network_requester_enabled', 'ip_packet_router_enabled', 'exit_policy']
        res = []
        res.insert(0, title)
        res.insert(1, "down")
        res.insert(2, "0")
        res.insert(3, "0")
        res.insert(4, "❌")
        res.insert(5, "❌")
        res.insert(6, "❌")
        ret = dict(zip(key, res))
        return ret
    bshealth = json.loads(str(BeautifulSoup(health, 'html.parser')))
    bsroles = json.loads(str(BeautifulSoup(roles, 'html.parser')))
    bsscore = json.loads(str(BeautifulSoup(score, 'html.parser')))
    bsexit = json.loads(str(BeautifulSoup(exit,'html.parser' )))
    res = getGateway(bshealth, bsscore, bsroles, bsexit, title)
    return  res

@app.route("/tupi<nodeid>")
def tupi(nodeid):
    identifier = utils.get_nodes_id(nodeid)
    info = urlopen("https://explorer.nymtech.net/api/v1/mix-node/" + identifier)
    bs = json.loads(str(BeautifulSoup(info, 'html.parser')))
    title = 'TupiNymQuim ' + nodeid
    res = getInfo(bs, title)
    return res

@app.route("/mixnodes/<nodeid>")
def mixnode(nodeid):
    info = urlopen("https://explorer.nymtech.net/api/v1/mix-node/"+ nodeid)
    bs = json.loads(str(BeautifulSoup(info, 'html.parser')))
    res = getInfo(bs)
    print(res)
    return res


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
