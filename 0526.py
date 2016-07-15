id2salary = {0:1000.0, 3:990, 1:1200.50}
names = ['Larry', 'Curly', '', 'Moe']

output = {names[i]:s for i in id2salary.keys() for (i,s) in id2salary.items()}
print(output)