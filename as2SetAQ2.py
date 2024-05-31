''' Write a python script which accepts 5 integer values and prints “DUPLICATES” 
if any of the values entered are duplicates otherwise it prints “ALL UNIQUE”.
Example: Let 5 integers are (32, 45, 90, 45, 6) then output “DUPLICATES” to be printed.  '''


a=[]
print("Enter 5 values..")
for i in range(5):
    num=input("Enter Numbers:")
    a.append(num)   #values inserted in list
print("List Elements:",a)

b=set(a)   # List element copy into set
print("Set Elements:",b)

if len(b) == len(a):     # List madhe duplicates yet nahe..
    print("Not Duplicate..")
else:
    print("DUPLICATES...")
    