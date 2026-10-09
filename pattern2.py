n=4
for i in range(1,n+1):
    if i%2!=0:
        print(' '*(n-i),"*"*((i*2)-1))
    else:
        print(' '*(n-i),"#"*((i*2)-1))