n = input("Enter Number:")
n = int(n)

cnteven = 0
cntodd = 0
cntzero = 0

while n != 0:
    digit = n % 10
    if digit == 0:
        cntzero += 1
    elif digit % 2 == 0:
        cnteven += 1
    else:
        cntodd += 1
    n //= 10
print("Number of zero :", cntzero)
print("number of even digits :", cnteven)
print("number of odd digits :", cntodd)
