import sys
sys.path.append('/root/NodesBot/')
import utils.gateways as gtw
import json
import utils.utils as utils
from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route("/gateway<gtwid>")
def gateways(gtwid):
    title = 'Gateway ' + gtwid + ' - ' + utils.get_gtw_id(gtwid).split()[2]
    gateway_id = utils.get_gtw_id(gtwid).split()[0]
    host = utils.get_gtw_id(gtwid).split()[1]
    res = gtw.get_gateways(title, gateway_id, host)
    return  res
    
@app.route("/tupi<nodeid>")
def nodes(nodeid):
    identifier = utils.get_nodes_id(nodeid)
    info = urlopen("https://explorer.nymtech.net/api/v1/mix-node/" + identifier)
    bs = json.loads(str(BeautifulSoup(info, 'html.parser')))
    title = 'TupiNymQuim ' + nodeid
    res = gtw.getInfo(bs, title)
    return res


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
