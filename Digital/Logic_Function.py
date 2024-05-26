import itertools

def Y(x,n):  # Logic Function

    if n == len(x):
        A = int(x[0])
        B = int(x[1])
        C = int(x[2])
        D = int(x[3])
        return (A | (~B))&((~C)&D)|A
    else:
        print("Number of inputs in logic function exceeds stated inputs")
        exit()

# Construct 4-bit truth table with boolean inputs

n = int(input("Number of inputs: "))

array = []
arr = [[0]*2]*2**n

for i in range(2**n):
    new_arr=[format(i,'0'+str(n)+'b'),0]
    arr[i]=new_arr


for i in range(len(arr)):
    arr[i][1]=Y(arr[i][0],n)
print("Truth Table:  \n")
for i in range(2**n):
    print(str(arr[i][0]) + "   " + str(arr[i][1]))


