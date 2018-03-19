#def factorial(n):
#    if n != 1:
#        n *= factorial(n-1)
#    return n

#print(factorial(3))
def bin_ones(numz):
    lyst_1 = []
    lyst_2 = []
    counter = 0
    number  = str(bin(numz))[2:]

    for num in number:
        lyst_1.append(num)

    for num in lyst_1:
        if num == '1':
            counter += 1
            lyst_2.append(counter)
        elif num == '0':
            if counter != 0:
                lyst_2.append(counter)
                counter = 0
            else:
                counter = 0
    n = 0
    for num in set(lyst_2):
        if num > n:
            n = num
    print(n)

print(bin_ones(44566787971))
