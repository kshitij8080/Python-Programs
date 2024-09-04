class A:
    def accept(self):
        self.name = input("Enter name:")
class B(A):
    def disp(self):
        print("Name = ", self.name)
ob = B()
ob.accept()
ob.disp()