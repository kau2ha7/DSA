def inserttion_sort(dlist):
 for i in range(1,len(dlist)):
  temp = dlist[i]
  j = i-1
  while j >= 0 and temp < dlist[j]:
   dlist[j+1]= dlist[j]
   j -=1
   dlist[j+1] = temp
l = [60,16,34,23,76]
inserttion_sort(l)
print(l)