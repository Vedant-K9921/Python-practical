m=int(input("Enter Num : "))
sum=0
while m>0:
    d=m%10
    sum=sum+d
    m=m//10
print("Sum :",sum)    