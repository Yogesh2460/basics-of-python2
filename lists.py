

def getodd(lst):
    oddlist=[]
    for i in lst:
        if i%2==1:
            oddlist.append(i)
    print(oddlist)#if it is  ifcond then it prints pyramid of odd numbers and if it is  for loop then it prints  odd numbers
    return#if return is for ifit will give [1] and if it is  for loop then it prints pyramid of odd numbers

if __name__=='__main__' :
    dlist=list(range(1,51))
    getodd(dlist)



#print([x for x in range(1,51) if x%2==1])
