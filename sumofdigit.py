m=abs(int(input("Enter Num : ")))
print(m)
sum=0
while m>0:
    d=m%10
    sum=sum+d
    m=m//10
print("Sum :",sum)