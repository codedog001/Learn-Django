def findMax(mylist):
    maxi = mylist[0]
    for i in mylist:
        if i > maxi:
            maxi = i
    return maxi