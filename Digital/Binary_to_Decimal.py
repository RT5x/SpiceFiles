import math
b = int(input("Input binary: "))
b_list=list(map(int, str(b)))
n = len(b_list)
sum = 0
for i in range(n):
    sum += b_list[i]*2**(n-i-1)

print("Decimal equivalent: ")
print(sum)

