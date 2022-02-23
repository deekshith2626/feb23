a=[]
n=int(input("ENTER THE ELEMENTS"))
for i in range(n):
    x=int(input())
    a.append(x)
min=a[0]
for i in range(1,n):
    if (min>a[i]):
        min=a[i]
        print("THE MINIMUM VALUE IS",min)
    else:
        print("THE GIVEN NUMBER IS MAX VALUE",a[i])
