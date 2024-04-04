import sys
sys.path.append('/root/NodesBot/')
import json
import utils.utils as utils
from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import Flask, request
from waitress import serve

app = Flask(__name__)

def getGateway(bshealth, bsscore, bsroles, bsexit, title):
    status = str(bshealth['status'])
    uptime = str(bshealth['uptime'])
    most_recent = str(bsscore['most_recent'])
    nr = str(bsroles['network_requester_enabled'])
    try:
        ip_router = str(bsroles['ip_packet_router_enabled'])
    except:
        ip_router = "False"
    exit = str(bsexit['enabled'])
    key = ['title', 'status', 'uptime', 'most_recent', 'network_requester_enabled', 'ip_packet_router_enabled', 'exit_policy']
    res = []
    res.insert(0, title.strip())
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

@app.route("/gateways/<title>")
def gateways(title):
    try:
        host = utils.get_host_by_identity_key(utils.get_data(), title)
        if (host == "Not Found"):
            raise Exception
        health = urlopen("http://"+host+":8080/api/v1/health", timeout=0.4)
        roles = urlopen("http://"+host+":8080/api/v1/roles")
        exit = urlopen("http://"+host+":8080/api/v1/network-requester/exit-policy")
        score = urlopen("https://validator.nymtech.net/api/v1/status/gateway/" + title + "/report")
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


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5001)
