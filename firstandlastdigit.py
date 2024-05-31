a = input("Enter Number:")
a = int(a)
s = 0

ldigit = a % 10
while a >= 10:
    a = a // 10
fdigit = a

s = fdigit + ldigit
print("Sum of first and last Digit is:", s)
