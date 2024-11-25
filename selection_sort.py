def selection_sort(dlist):
    n = len(dlist)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if dlist[j] < dlist[min_idx]:
                min_idx = j
        dlist[i],dlist[min_idx] = dlist[min_idx],dlist[i]
l = [20,40,56,70,30]
selection_sort(l)
print(l)