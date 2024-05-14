import json
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_identity_key():
    try:
        with open("/root/NodesBot/utils/gateways.txt") as file:
            key = file.readlines()
        return key
    except IOError as e:
        print("Error:", e)
        return "Not found"

def set_identity_key(identity_key):
    if (check_key_exists(identity_key) == 1):
        return ("Gateway already exist!")
    remove_blank_lines() 
    file = open("/root/NodesBot/utils/gateways.txt", 'a')
    file.write("\n")
    file.write(identity_key)
    return ("Gateway added successfully!")
            
def remove_identity_key(identity_key):
  filename = "/root/NodesBot/utils/gateways.txt"
  if (check_key_exists(identity_key) == 1):
    with open(filename, 'r') as read_file, open(filename + ".new", 'w') as write_file:
        for line in read_file:
            if line.strip() != identity_key:
                write_file.write(line)
    os.replace(filename + '.new', filename)
    return ("Gateway Successfully removed!")
  return ("Gateway not found!")
    
def remove_blank_lines():
    filename = "/root/NodesBot/utils/gateways.txt"
    with open(filename, 'r') as infile, open(filename + '.new', 'w') as outfile:
        for line in infile:
            if not line.strip():
                continue
            outfile.write(line)
    os.replace(filename + '.new', filename)

def check_key_exists(identity_key):
    with open("/root/NodesBot/utils/gateways.txt", 'r') as read_file:
        for line in read_file:
            if line.strip() == identity_key:
                return (1)
        return (-1)


def get_gtw_id(gtwid):
    try:
        with open("/root/NodesBot/utils/gtw.txt") as file:
            gtws_id = file.readlines()
        return gtws_id[(int)(gtwid) - 1]
    except IOError as e:
        print("Error:", e)
        return "Not found"

def get_nodes_id(nodeid):
    try:
        with open("/root/NodesBot/utils/nodes.txt") as file:
            nodes_id = file.readlines()
        return nodes_id[(int)(nodeid) - 1]
    except IOError as e:
        print("Error:", e)
        return "Not found"

def get_size_gateways():
    keys =  get_identity_key()
    return (len(keys))

def get_data():
    try:
        info = urlopen("https://validator.nymtech.net/api/v1/gateways/described")
        data = json.loads(str(BeautifulSoup(info, 'html.parser')))
        return data
    except:
        print("Error: Data Invalid")
        return None

def get_host_by_identity_key(data, identity_key):
    for item in data:
        if item["bond"]["gateway"]["identity_key"] == identity_key:
            return item["bond"]["gateway"]["host"]
    return "Not Found"

def get_all_host_by_identity_key(data, identity_key):
    for item in data:
        if item["bond"]["gateway"]["identity_key"] == identity_key:
            return write_host(identity_key, item["bond"]["gateway"]["host"])
    return write_host(identity_key, None)


def write_host(identity_key, value):
    file = open("/root/NodesBot/utils/hosts.txt", 'a')
    if (value):
        file.write(identity_key)
        file.write(" : " + str(value) + "\n")
    else:
        file.write(identity_key)
        file.write(" : Host not found\n")


def create_list_hosts(size):
    i = 0
    while (i < size):
        get_all_host_by_identity_key(get_data(), get_identity_key()[i].strip())
        i = i + 1