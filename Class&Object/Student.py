class student:
    def accept(self):
        self.rno = input("Enter Roll no:")
        self.name = input("Enter Name:")
        self.per = input("Enter Percentage:")
    def display(self):
        print("Roll no = ", self.rno)
        print("Name = ", self.name)
        print("Percentage = ", self.per)
ob = student()
ob.accept()
ob.display()
