class student:
    def accept(self):
        self.rno = input("Enter Student roll no : ")
        self.name = input("Enter Student name : ")
        self.per = input("Enter Student percentage : ")
    def disp(self):
        print("Roll no = ", self.rno)
        print("Name = ", self.name)
        print("Percentage = ", self.per)
a1 = []
n = int(input("Enter limit :"))
for i in range(0, n):
    ob = student()
    ob.accept()
    a1.append(ob)
for i in range(0, n):
    a1[i].disp()