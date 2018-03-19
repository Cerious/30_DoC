dict_1 = {'sam': 99912222, 'tom': 11122222, 'harry': 12299933}

def checker(name):
    if name in dict_1.keys():
        print(str(name) + '=' + str(dict_1[name]))
    else:
        print('Not found')



checker('sam')
checker('edward')
checker('harry')
