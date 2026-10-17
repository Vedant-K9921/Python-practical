f=open("sample.txt")
con=f.read()
vowels="aeiouAEIOU"
vowcount=0
for char in con:
    if char in vowels:
        vowcount+=1

print("total vowel : ",vowcount)
f.close()