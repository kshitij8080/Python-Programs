class Team:
    def __init__(self, Team_name):
        self.Team_name = Team_name
class Dev(Team):
    def __init__(self, Team_name, role):
        super().__init__(Team_name)
        self.role = role
class Employee(Dev):
    def __init__(self, Team_name, role, employee_name):
        super().__init__(Team_name, role)
        self.emloyee_name = employee_name
    def disp(self):
        print("Team Name = ", self.Team_name)
        print("Role = ", self.role)
        print("Employee Name = ", self.emloyee_name)
ob = Employee("Development", "Full-Stack Developer", "sai")
ob.disp()