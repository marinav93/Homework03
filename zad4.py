def myMax(lst):

    if len(lst) == 1:
        return lst[0]

    subMax = myMax(lst[1:])
    if lst[0] > subMax:
        return lst[0]
    else:
        return subMax


myList = [1,-1,2,-2,5,15,-91]
print('The maximum of myList is', myMax(myList))
