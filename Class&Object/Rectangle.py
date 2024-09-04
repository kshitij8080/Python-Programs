class Rectangle:
        def accept(self,height):
            self.l = float(input("Enter Length:"))
            self.w = float(input("Enter Width:"))
            self.h = height
        def compute(self):
            area = self.l * self.w
            print("area of rectangle:", area)
            volume = self.l * self.w * self.h
            print("volume of rectangle:", volume)
ob = Rectangle()
ob.accept(5)
ob.compute()
