dct={'a':'A', 'b':'B', 'c':'C'}
keylist=['b','c','a']

dict2list = [v for i in range(0,len(keylist)) for v in dct[keylist[i]]]
print(dict2list)