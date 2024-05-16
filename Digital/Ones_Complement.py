
# Ones complement

bin = (input("Input binary number: "))
x=list(map(int,str(bin)))
i = 0
while i <= len(x)-1:
    if x[i]==1:
        x[i]=0
        i+=1
    else:
        x[i]=1
        i+=1

s = ''.join(map(str, x))

print("Ones complement: \n")

print(s)

sum = 0
for i in range(len(x)):
    sum += x[i]*2**(len(x)-i-1)

sum = sum + 1

d1_int = int(sum)


arr_bin = []

while d1_int >= 1:
    if d1_int % 2 != 0:
        
        d1_int = (d1_int-1)/2
        arr_bin.append(1)
 
    else:
        d1_int = d1_int/2
        arr_bin.append(0)
    


arr_bin.reverse()

result_twos = int(''.join(map(str,arr_bin)))


print("Twos Complement: \n")
print(result_twos)