import random

def getnewmembers():
    try:
        arq = open("/home/scraper/newmembers.txt")
    except:
        arq = open("/home/scraper/newmembers.txt", "w+")
        arq.write("0\n")
        return (0)
    i = 0
    result = (arq.read())
    size = len(result)
    value = ""
    while (i < size - 1):
        value = value + result[i]
        i = i + 1;

    try:
        return (int(value))
    except:
        return (0)

def setnewmembers(value):
    arq =  open("/home/scraper/newmembers.txt", "w+")
    arq.write(str(value) + "\n")

def addnewmember(value):
    arq = open("/home/scraper/listmembers.txt", "a+")
    arq.write(value + "\n")

def listnewmember(index):
    arq = open('/home/scraper/listmembers.txt', 'r')
    names = arq.readlines()
    ret = []
    for name in names:
        ret.append(name)
    return (ret[index])

def randommember():
    arq = open('~/listmembers.txt', 'r')
    names = arq.readlines()
    ret = []
    for name in names:
        ret.append(name)
    random.shuffle(ret)
    winner = random.choice(ret)
    return (winner)

def eraselist():
    arq = open('/home/scraper/listmembers.txt', 'w+')
    arq.write("")
    new =  open("/home/scraper/newmembers.txt", "w+")
    new.write("0\n")
