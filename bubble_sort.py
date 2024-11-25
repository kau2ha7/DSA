def bubble_sort(dlist):
    for i in range(1,len(dlist)):
        for j in range(len(dlist)-i):
            if dlist[j] > dlist[j+1]:
                dlist[j],dlist[j+1] = dlist[j+1],dlist[j]
def modified_bubble_sort(data_list):
    for i in range(1,len(data_list)):
        flag=False
        for j in range(len(data_list)-i):
            if data_list[j]>data_list[j+1]:
                data_list[j],data_list[j+1] = data_list[j+1],data_list[j]
                flag=True
        if not flag:
            break

l = [20,50,18,60,40]
bubble_sort(l)
print(l)