def merge_sort(dlist):
      if len(dlist)>1:
            mid = len(dlist)//2
            leftSide = dlist[:mid]
            rightSide = dlist[mid:]
            merge_sort(leftSide)
            merge_sort(rightSide)
            i=j=k=0
            while i < len(leftSide) and j < len(rightSide):
                  if leftSide[i] < rightSide[j]:
                        dlist[k] = leftSide[i]
                        i +=1
                  else:
                        dlist[k] = rightSide[j]
                        j +=1
                  k +=1
            while i < len(leftSide):
                  dlist[k] = leftSide[i]
                  i +=1
                  k +=1
            while j < len(rightSide):
                  dlist[k] = rightSide[j]
                  j +=1
                  k +=1

      

myL = [10,50,5,18,25,45,69,87]
merge_sort(myL)
print(myL)