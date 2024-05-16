#import math
from math import log10

d1 = float(input("Input decimal number: "))

d1_int = int(d1)
d1_dec = d1 - d1_int
n = int(log10(d1_int)/log10(2))
i = 0
arr_bin = []
d1_int_op=d1_int

while d1_int_op >= 1:
    if d1_int_op % 2 != 0:
        
        d1_int_op = (d1_int_op-1)/2
        arr_bin.append(1)
    
    else:
        d1_int_op = d1_int_op/2
        arr_bin.append(0)
       



arr_bin.reverse()

result1 = int(''.join(map(str,arr_bin)))

arr_dec=[]
j = 0
while j <= n+2:
    if d1_dec*2 < 1:
        d1_dec = d1_dec*2
        arr_dec.append(0)
        j+=1
    elif d1_dec*2 >= 1:
        d1_dec = d1_dec*2 - 1
        arr_dec.append(1)
        j+=1
    else:
        j+=1


result2 = int(''.join(map(str,arr_dec)))
print("Binary Equivalent: ")
print(str(result1)+"."+str(result2))