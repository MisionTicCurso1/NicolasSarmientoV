

l=[{'1':{'A':'a', 2:'b'}},{'1':{'A':'c',4:'d'}}]



for i in range(len(l)):
    for x in l[i]:
        print(l[i][x]['A'])