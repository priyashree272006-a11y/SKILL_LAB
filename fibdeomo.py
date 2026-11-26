n=int(input("enter the term:"))
count=0
a=0
b=1
while count<n:
    print(a)
    c=a+b
    a=b
    b=c
    count+=1
print("total iterations:",count)


