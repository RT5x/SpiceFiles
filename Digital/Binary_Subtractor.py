import math
from math import log10
print("Binary Subtractor ")
b1 = int(input("Input first binary number: "))
b2 = int(input("Input second binary number: "))
b1_list=list(map(int, str(b1)))
b2_list=list(map(int, str(b2)))
n1 = len(b1_list)
n2 = len(b2_list)
sum1 = 0
sum2 = 0
for i in range(n1):
    sum1 += b1_list[i]*2**(n1-i-1)
for i in range(n2):
    sum2 += b2_list[i]*2**(n2-i-1)

sum = sum1-sum2

d1_int_op = int(sum)


n = int(log10(d1_int_op)/log10(2))

arr_bin = []


while d1_int_op >= 1:
    if d1_int_op % 2 == 1:
        
        d1_int_op = (d1_int_op-1)/2
        arr_bin.append(1)
        

    elif d1_int_op % 2 == 0:
        d1_int_op = d1_int_op/2
        arr_bin.append(0)
        


    else:
        continue


arr_bin.reverse()

result1 = int(''.join(map(str,arr_bin)))
print(str(b1) + " - " + str(b2) + " = ")


print(result1)