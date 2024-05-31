n=int(input("Enter number:"))
sum=0
temp=n

while n > 0:
    r = n % 10
    sum = (sum * 10) + r
    n = n // 10

if temp == sum:
    print("Number is Palindrome...")
else:
    print("Number is NOT Palindrome...")