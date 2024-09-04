class Circle:
    def area(self):
        self.radius = float(input("Enter radius:"))
        a = 3.14 * self.radius * self.radius
        print("Area of circle = ", a)
    def circumference(self):
        self.radius = float(input("Enter radius:"))
        a = 2 * 3.14 * self.radius
        print("circumference of circle = ", a)
ob = Circle()
ob.area()
ob.circumference()
