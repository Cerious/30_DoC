import sys
def is_int(strg):
    booly  = []
    for i in strg:
        all_syms = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '?', '>', '<', ':', ';', '{', '}', '}',
        '{', '|', '=', '-', '_', '+', '!', '@', '#', '$', '%', '^', '&', '*', '(',
        ')', ',', '.']
        res = i in all_syms
        booly.append(res)
    if True in booly:
        return False
    else:
        return True






def int_change(strg):
    arr = []
    if is_int(strg) == True:
        arr.append(int(strg))
    else:
        try:
            int(strg)
        except ValueError:
            arr.append('Bad String')

    return arr[0]



print(int_change('34789e48'))
