def getnewmembers():
    arq = open("newmembers.txt")
    i = 0;
    result = (arq.read())
    size = len(result)
    value = ""
    while (i < size - 1):
        value = value + result[i]
        i = i + 1;

    return (int(value))


def setnewmembers(value):
    arq =  open("newmembers.txt", "w+")
    arq.write(str(value) + "\n")

def addnewmember(value):
    arq = open("listmembers.txt", "a+")
    arq.write(value + "\n")

def listnewmember(index):
    arq = open('listmembers.txt', 'r')
    names = arq.readlines()
    ret = []
    for name in names:
        ret.append(name)
    return (ret[index])
