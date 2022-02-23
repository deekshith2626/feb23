l=[]
n=int(input("ENTER THE GIVEN NUMBERS " ))
for i in range (n):
    x=int(input())
    l.append(x)

for i in range(n-1,n-n-1,-1):
    print("GIVEN VALUE IS REVERSED",l[i])
