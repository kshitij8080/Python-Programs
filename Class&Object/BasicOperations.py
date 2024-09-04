class Calculator:
    def addition(self, a, b):
        return a + b
    def subtraction(self, a, b):
        return a - b
    def multiplication(self, a, b):
        return a * b
    def division(self, a, b):
        return a / b
        
ob = Calculator()
print("Addition= ", ob.addition(10, 20))
print("subtraction =", ob.subtraction(20, 10))
print("Multiplication =", ob.multiplication(10, 5))
print("Division =", ob.division(10, 20))
