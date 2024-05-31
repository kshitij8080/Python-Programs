start_number = int(input("Enter Start Number:"))
end_number = int(input("Enter End number:"))
for i in range(start_number, end_number + 1):
    print("\n")
    for n in range(1, 11):
        print(i*n, end=" ")
