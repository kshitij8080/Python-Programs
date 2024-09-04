class Area:
    def accept(self, side=0, base=0, height=0):
        self.side = side
        self.base = base
        self.height = height
class square(Area):
    def disp_square(self):
        ans = self.side * self.side
        print("Area of square = ", ans)
class triangle(Area):
    def disp_triangle(self):
        ans = 0.5 * (self.base * self.height)
        print("Area of triangle = ", ans)
ob = square()
ob.accept(side=5)
ob.disp_square()
ob1 = triangle()
ob1.accept(base=10, height=3)
ob1.disp_triangle()