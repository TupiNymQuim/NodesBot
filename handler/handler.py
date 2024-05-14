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
    key = ['title', 'status', 'uptime', 'most_recent', 'config_score']
    res = []
    res.insert(0, title)
    res.insert(1, status)
    res.insert(2, uptime)
    res.insert(3, most_recent)
    if (nr == "True" and ip_router == "True" and exit == "True"):
        res.insert(4, "🐼")
    else:
        res.insert(4, "❌")
    ret = dict(zip(key, res))
    return ret

@app.route("/gateway<gtwid>")
def gateways(gtwid):
    title = 'Gateway ' + gtwid + ' - ' + utils.get_gtw_id(gtwid).split()[2]
    gateway_id = utils.get_gtw_id(gtwid).split()[0]
    host = utils.get_gtw_id(gtwid).split()[1]
    try:
        health = urlopen("http://"+host+":8080/api/v1/health", timeout=0.4)
        roles = urlopen("http://"+host+":8080/api/v1/roles")
        exit = urlopen("http://"+host+":8080/api/v1/network-requester/exit-policy")
        score = urlopen("https://validator.nymtech.net/api/v1/status/gateway/"+gateway_id+"/report")
    except:
        key = ['title', 'status', 'uptime', 'most_recent', 'config_score']
        res = []
        res.insert(0, title)
        res.insert(1, "down")
        res.insert(2, "0")
        res.insert(3, "0")
        res.insert(4, "❌")
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
    return res


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
