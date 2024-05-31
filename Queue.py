'''
implement the concept of queue
insert-end
delete-beginning
display
'''
 
a1 = []
ch = 0
while ch != 4:
    print("\n 1-insert \n 2-delete \n 3-display \n 4-exit")
    ch = int(input("Enter Choice:"))
    if ch == 1:
        num = input("Enter Number:")
        a1.append(num)
        print(a1)
    elif ch == 2:
        del a1[0]
        print(a1)
    elif ch == 3:
        print(a1)
    else:
        print("invalid Choice....")
