def quick_sort(dlist):
    if len(dlist) <=1:
        return dlist
    else:
        pivot = dlist[0]
        lesser = [i for i in dlist[1:] if i < pivot]
        greater = [i for i in dlist[1:] if i > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)

                
      
l = [50,65,85,23,4,5,68,15,23]
print(quick_sort(l))