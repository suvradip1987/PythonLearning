from Employee import Employee


class PermanentEmployee(Employee):
    def __init__(self, first_name, last_name, emp_id):
        super().__init__(first_name, last_name)
        self.empId=emp_id


    def say_hello(self):
        print("I am Permanent Employee")

    def print_emp_name(self):
        print("Employee Name :"+self.first_name + " " + self.last_name)

emp1 = Employee("Suvradip", "Mondal")
emp1.print_emp_name()

permEmp = PermanentEmployee("Hati", "Mondal", "smondal1")
permEmp.print_emp_name()
permEmp.say_hello()
permEmp.say_hello()
