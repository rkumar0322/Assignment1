import pandas as pd


def parse_row(strparse):
    row = strparse[1:-1].split("> <")
    return row

def parse_list(lostr):
    lol = []
    largest_schema = None
    len_largest = 0
    for i in range(0,500):
        list1 = parse_row(lostr[i])
        if len(list1) > len_largest:
            len_largest = len(list1)
            largest_schema = list1
        lol.append(list1)
        if i + 1 == len(lostr):
            break
    return lol, largest_schema

def create_table(lol, largest_schema):
    print(lol)
    print(largest_schema)
    fields = [[] for i in largest_schema]
    for i in lol:
        for x in range(0,len(largest_schema)):
            if type(infer_type(largest_schema[x])) == type(infer_type(i[x])):
                fields[x].append(infer_type(i[x]))
            else:
                fields[x].append(None)
            if x + 1 == len(i):
                break
    return pd.DataFrame(fields).transpose()

def parsefile():
    f = open("data.txt","r")
    list = []
    line1 = f.readlines()
    return [x.strip() for x in line1]


def infer_type(x):
    if x == "":
        return x
    elif x[0] == "\"" and x[-1] == "\"":
        return x[1:-1]
    elif x == "1":
        return True
    elif x == "0":
        return False
    elif x[0] == "+":
        if x[1] in "1234567890":
            if "." in x:
                return float(x[1:len(x)])
            else:
                return int(x[1:len(x)])
    elif x[0] == "-":
        if x[1] in "1234567890":
            if "." in x:
                return float(x[1:len(x)])*-1
            else:
                return int(x[1:len(x)])*-1
    elif x[0] in "1234567890":
        if "." in x:
            return float(x[0:len(x)])
        else:
            return int(x[0:len(x)])
    else:
        return x





print(create_table(parse_list(parsefile())[0],parse_list(parsefile())[1]))

