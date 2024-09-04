class Emp:
    def accept(self, rno, name, per):
        self.rno = rno
        self.name = name
        self.per = per
class B(Emp):
    def disp(self):
        print("Roll no = ", self.rno)
        print("Name = ", self.name)
        print("Percentage = ", self.per)
ob = B()
ob.accept(101,"om",78)
ob.disp()