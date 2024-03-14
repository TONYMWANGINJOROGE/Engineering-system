class Employee:
    second_name = 'Felix'
    raise_amt = 3



    def __init__(self,name,gender,salary):
        self.name = name
        self.gender = gender
        self.salary =salary
        self.email = name+'@gmail.com'
    def fullname (self):
        return self.name
    def salary_increase(self):
        self.salary =int(self.salary *self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


emp1 = Employee('Felix','Male',50000)
emp2 = Employee('Peter','Male',6066666)
print(emp1.name)
print(emp1.name)
print(emp1.email)
print(emp2.email)
print(f'{emp1.name} is {emp1.gender} and earns {emp1.salary}')
print(f'{emp2.name} is {emp2.gender} and earns {emp2.salary}')
emp1.salary_increase()
print(emp1.salary)

print(f'{emp1.name} is {emp1.gender}')
print(emp2.salary)
emp2.salary_increase()
print(emp2.salary)
Employee.raise_amt = 5

print(emp1.raise_amt)
print(Employee.raise_amt)

Employee.set_raise_amt(30)
print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)




class Students:
    def __init__(self,firstname,lastname,Geo,Phyc):
        self.firstname = firstname
        self.lastname = lastname
        self.Geo = Geo
        self.Phyc = Phyc
    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    def apply_total(self):
        return self.Geo+self.Phyc
        self.total = self.Geo+self.Phyc
        return self.total
std1 = Students('Tony','Njoroge',90,80)
std2 = Students('Burkard','Karl',92,88)
print(f'{std1.firstname} {std1.lastname} has {std1.Geo} in Geography and {std1.Phyc} in physics and the total is {std1.apply_total()}')
print(f'{std2.firstname} {std2.lastname} has {std2.Geo} in Geography and {std2.Phyc} in physics and the total is {std2.apply_total()}')

print(std1.apply_total())
print(std2.apply_total())

class Developers(Students):
    def __init__(self,firstname,lastname,Geo,Phyc,age,stream):
        super().__init__(firstname,lastname,Geo,Phyc)
        self.age = age
        self.stream =stream

Developers1 = Developers('Myles','Kirubi',90,80,25,'form4 b')
Developers2 = Developers('Cerline','wanja',90,80,25,'form4 a')
# print(f'{std1.firstname} {std1.lastname} has {std1.Geo} in Geography and {std1.Phyc} in physics and the total is {std1.apply_total()} and he is {Developers1.age}')

class Footballers:
    def __init__(display,Name,Gender,Age):
        display.fullname = Name
        display.Gender = Gender
        display.Age =Age
    def fullname(display):
        return f"{display.fullname()}"

ply1=Footballers('Peter','male',32)
ply2=Footballers('Faith','female',29)

class  Position(Footballers):
    def __init__(display,Name,Gender,Age,position):
        super().__init__(Name,Gender,Age)
        display.position = position
pst1=Position('Peter','male',32,'center')
pst2=Position('Faith','female',29,'defense')
 # print(pst1)


