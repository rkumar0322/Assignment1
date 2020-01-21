import pandas as pd


def parse_row(strparse):
    row = strparse[1:-1].split("> <")
    return row

def parse_list(lostr):
    lol = []
    for i in lostr:
        list1 = parse_row(i)
        lol.append(list1)
    return pd.DataFrame(lol)

def parsefile():
    f = open("data.txt","r")
    list = []
    line1 = f.readlines()
    return [x.strip() for x in line1]

print(parse_list(parsefile()))

##print