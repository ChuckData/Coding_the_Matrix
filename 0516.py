S = {-4, -2, 1, 2, 5, 0}

S_List = [(i, j, k) for i in S for j in S for k in S if i+j+k == 0 if (i, j, k) != (0, 0, 0)]

print(S_List[0])