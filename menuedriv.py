n=int(input("Enter Number:"))

print("1-Square \n 2-Cube \n 3-Even Odd")
ch=int(input("Enter Choice:"))

if ch == 1:
    print("Square=",n*n)
elif ch == 2:
    print("Cube=",n*n*n)
elif ch == 3:
    if n % 2 == 0:
        print("Number is Even..")
    else:
        print("Number is Odd...")