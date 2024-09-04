class Circle:
    def accept(self, radius):
        self.radius = radius
class Area(Circle):
    def disp(self):
        ans = 3.14 * self.radius * self.radius
        print("Area of circle = ", ans)
ob = Area()
ob.accept(3)
ob.disp()