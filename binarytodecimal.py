b = int(input("Enter Binary Number:"))
decimal = 0
base = 1
binary_num = b
while b > 0:
    rem = b % 10
    decimal = decimal + rem * base
    b = b // 10
    base = base * 2

print("Binary Number is:", binary_num)
print("\n decimal number is:", decimal)
