# import math
# class Circle:
#     def __init__(self, rad):
#         self.rad = rad

#     @property
#     def area(self):
#         area = math.pi*(self.rad**2)
#         print (area)



# c1 = Circle(5)
# print(c1.area)

# c1.rad = 3
# print(c1.area)



class Employee:
    def __init__(self, role, dep, sal):
        self.role = role
        self.dep = dep
        self.sal = sal

    def showDetails(self):
        print("Role =", self.role)
        print("Department =", self.dep)
        print("Salary =", self.sal)


class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", 60000)


e1 = Engineer("Rock", 23)
e1.showDetails()