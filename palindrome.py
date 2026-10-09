nm=input("Enter name : ")
nm=nm.lower().replace(" ","")
if nm==nm[::-1]:
    print("Pakindrome")
else:
    print("Not Palindrome")