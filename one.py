lst = [1,4,5,4,3,5,2,4,2,4,3]
for i in lst:
    if lst[i] > lst[i+1]:
       lst.remove(i)
for i in lst:
    if lst[i] > lst[i+1]:
        max = lst[i+1]
        print(max)
