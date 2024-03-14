class Student:
    name= 'Tony'
    age= 20
print(Student . name)
print(Student.age)
print(f'Name:{Student.name} Age: {Student.age}')

class Employees:
    name= 'Tony'
    location= 'New York'
    salary= '100000$'
print(f'Name:{Employees.name} salary:{Employees.salary} location:{Employees.location}')


# class Parents:
#     first_name= 'Tony'
#     last_name= 'Mwangi'
# parent1=Parents()
# print(parent1.first_name,parent1.last_name)
#
# class Parent:
#     first_name= 'Kevin'
#     last_name= 'Wanjiru'
# parent2=Parent()
# print(parent2.first_name,parent2.last_name)

class Parent:
    def __init__(self,first_name,last_name):
        self.first_name= first_name
        self.last_name= last_name
parent1=Parent('Alex','Puchitino')
print(f"parent1's first name is " f" {parent1.first_name}  and last name is " f" {parent1.last_name} ")
parent2=Parent('Kevin','Wanjiru')
print(parent2.first_name,parent2.last_name)

class Presidents:
    def __init__(self,first_name,last_name):
        self.first_name= first_name
        self.last_name= last_name
president1=Presidents('Jomo','Kenyatta')
print(f"president1's first name is " f"{president1.first_name} and last name is " f"{president1.last_name}")
president2=Presidents('Daniel','Moi')
print(f"president2's first name is "f"{president2.first_name} and last name is "f"{president2.last_name}")

class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name= first_name
        self.last_name= last_name
        self.age= age
    def full_name (self):
        print(f"{self.first_name} {self.last_name} {self.age} years old")
person1=Person('Jomo','Kenyatta',age=21)
print(person1.first_name,person1.last_name,person1.age)
print(person1.full_name())
person2=Person('Daniel','Moi',age=30)
print(person2.first_name,person2.last_name,person2.age)