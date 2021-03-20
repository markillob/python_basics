# s_li = sorted(list) create a new list 
#list.sort()  sort current list , just work in LIST
#sorted(li, key=abs) get the absolute value
#
#  sorted(list,reverse=True)

class Employee():
    def __init__( self, name, age, salary):
        self.name = name
        self.age = age 
        self.salary = salary
    
    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl','78',7000)
e2 = Employee('Thomas','45', 500)

employees = [e1, e2]

def e_sort(Employee):
    return Employee.age

s1_employees = sorted(employees, key = lambda e: e.age)
print(s1_employees)




