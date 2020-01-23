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

def parsefile(f,start=0,end=100):
    f = open(f,"r")
    f.seek(start)
    line1 = f.read(end)
    if start > 0:
        firstbreak = line1[0:end].index("\n")
        line1 = line1[firstbreak+1:len(line1)]
    line1 = line1.split("\n")
    if start > 0:
        line1 = line1[0:-1]
    return [x.strip() for x in line1]


def infer_type(x):
    if x == "":
        return None
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


def print_col_type(df,col):
    value = None
    for i in df[col]:
        if i is not None:
            value = i
            break
    return type(value)

def is_missing_idx(df,col,offset):
    if df[col][offset] is None:
        return True
    else:
        return False

def print_col_idx(df,col,offset):
    return df[col][offset]





table =  create_table(parse_list(parsefile("newtxt.txt"))[0],parse_list(parsefile("newtxt.txt"))[1])


print(print_col_type(table,0))
print(print_col_type(table,2))
print(is_missing_idx(table,2,0))
print(is_missing_idx(table,2,1))
print(is_missing_idx(table,2,2))
print(is_missing_idx(table,1,2))
print(print_col_idx(table,2,0))
table = create_table(parse_list(parsefile("newtxt.txt",5))[0],parse_list(parsefile("newtxt.txt",5))[1])
print(print_col_idx(table,1,0))


