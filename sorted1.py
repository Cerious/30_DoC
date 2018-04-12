

def swap(lyst, el1, el2):
    newPosEl1 = lyst.index(el2)
    newPosEl2 = lyst.index(el1)
    lyst.remove(el1)
    lyst.remove(el2)
    if  newPosEl2 != abs(newPosEl2) or newPosEl1 != abs(newPosEl1):
        lyst.insert(newPosEl1, el1)
        lyst.insert(newPosEl2, el2)
    elif newPosEl2 < newPosEl1:
        lyst.insert(newPosEl1-1, el1)
        lyst.insert(newPosEl2, el2)
    elif newPosEl2 > newPosEl1:
        lyst.insert(newPosEl1, el1)
        lyst.insert(newPosEl2, el2)


def organize(lyst):
    swaps = 0
    for j in lyst:
        for i in lyst:
            if lyst.index(i) == len(lyst)-1:
                pass
            elif i > lyst[lyst.index(i)+1]:
                swap(lyst, i, lyst[lyst.index(i)+1])
                swaps += 1

    print("Array is sorted in " + str(swaps) + " swaps")
    print("First Element:" + str(lyst[0]))
    print("Last Element:" + str(lyst[-1]))






lyst = [1,4,6,2,3,8]
organize(lyst)
print(lyst)
