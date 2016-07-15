dlist = [{'Bilbo':'Ian','Frodo':'Elijah'}, {'Bilbo':'Martin','Thorin':'Richard'}]

dlist_result = [dlist[x]['Frodo'] if 'Frodo' in dlist[x] else 'Not Present' for x in list(range(len(dlist)))]

print(dlist_result)