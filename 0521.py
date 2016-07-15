dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]

dlist_result = [dlist[x]['James'] for x in list(range(len(dlist)))]

print(dlist_result)