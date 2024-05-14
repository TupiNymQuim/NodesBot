import sys
sys.path.append('/root/NodesBot/')
import json
import utils.utils as utils
from bs4 import BeautifulSoup
from urllib.request import urlopen

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

def get_gateways(title, gateway_id, host):
    try:
        if (host == "Not Found"):
            raise Exception
        health = urlopen("http://"+host+":8080/api/v1/health", timeout=0.4)
        roles = urlopen("http://"+host+":8080/api/v1/roles")
        exit = urlopen("http://"+host+":8080/api/v1/network-requester/exit-policy")
        score = urlopen("https://validator.nymtech.net/api/v1/status/gateway/"+gateway_id+"/report")
    except:
        key = ['title', 'status', 'uptime', 'most_recent', 'version', 'config_score']
        res = []
        res.insert(0, title)
        res.insert(1, "down")
        res.insert(2, "0")
        res.insert(3, "0")
        res.insert(4, "Not Found")
        res.insert(5, "❌")
        ret = dict(zip(key, res))
        return ret
    bshealth = json.loads(str(BeautifulSoup(health, 'html.parser')))
    bsroles = json.loads(str(BeautifulSoup(roles, 'html.parser')))
    bsscore = json.loads(str(BeautifulSoup(score, 'html.parser')))
    bsexit = json.loads(str(BeautifulSoup(exit,'html.parser' )))
    res = getGateway(bshealth, bsscore, bsroles, bsexit, title)
    return  res
    
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