# data = 1,3,5,4,7,8,10,10,3
data = [['a','c'],['a','e'],['d','a'],['b','c'],['c','b'],['d','c']]
def main(x):
    sorted_list = []
    remain = []
    unique = []
    for i in x:
        y = sorted(i)
        sorted_list.append(y)
    #print(sorted_list)
    for v in x:
        if v in sorted_list:
            unique.append(v)
        else:
            remain.append(v)
    #print(unique)
    #print(remain)
    for j in remain:
        if sorted(j) not in unique:
            unique.append(j)
    print(x, sep='\n',)
    print(unique)


if __name__ == '__main__': main(data)
