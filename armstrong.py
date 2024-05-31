n = int(input("Enter Number:"))
s = 0
temp = n

while n > 0:
    r = n % 10
    s = s+(r*r*r)
    n = n // 10
if temp == s:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")
    