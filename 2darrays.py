arr = [[-1, -1, 0, -9, -2, -2],[-2, -1, -6, -8, -2, -5,],[-1, -1, -1, -2, -3, -4],[-1, -9, -2, -4, -4, -5],[-7, -3, -3, -2, -9, -9],[-1, -3, -1, -2, -4, -5]]
great_arr = []
nums = []
eye = 0

for i in arr:
    jay = 0
    for j in i:
        if jay == 4:
            jay = 0
        if eye < 4 and jay < 4:
            sub_arr = []
            sub_arr.append(i[jay])
            sub_arr.append(i[jay+1])
            sub_arr.append(i[jay+2])
            sub_arr.append(arr[eye+1][jay+1])
            sub_arr.append(arr[eye+2][jay])
            sub_arr.append(arr[eye+2][jay+1])
            sub_arr.append(arr[eye+2][jay+2])
            great_arr.append(sub_arr)
            num = sum(sub_arr)
            nums.append(num)
            jay += 1
            #print ('Eye: ' + str(eye))
    eye += 1

final = -1000
for num in nums:
    
    print(str(num) + ' > '+ str(final)+ ': ' + str(num > final) )
    if num > final and num > 0:
        final = num
    elif num > final and num < 0:
        final = num

print(great_arr)
print (nums)
print(final)
