import json
import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup
sys.path.append('/root/NodesBot/')
import utils.gateways as gtw
import utils.utils as utils
from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route("/gateways/<title>")
def gateways(title):
    host = utils.get_host_by_identity_key(utils.get_data(), title)
    res = gtw.get_gateways(title, title, host)
    return (res)

    
@app.route("/mixnodes/<nodeid>")
def mixnode(nodeid):
    info = urlopen("https://explorer.nymtech.net/api/v1/mix-node/"+ nodeid)
    bs = json.loads(str(BeautifulSoup(info, 'html.parser')))
    res = getInfo(bs)
    return res


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5001)
