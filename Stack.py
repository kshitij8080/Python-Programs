# implement the concept of stack

a1 = []
ch = 0
while ch != 4:
    print("\n 1-insert \n 2-delete \n 3-disp \n 4-exit")
    ch = int(input("Enter Choice:"))
    if ch == 1:
        num = input("Enter Number:")
        a1.append(num)
        print(a1)
    elif ch == 2:
        if len(a1) == 0:
            print("Stack is empty...")
        else:
            del a1[-1]
            print(a1)
    elif ch == 3:
        print(a1)
    else:
        print("Invalid choice...")
