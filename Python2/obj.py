class Staff:
    def __init__(self,Name,number,Location,school):
        self.Name = Name
        self.number = number
        self.Location =Location
        self.school = school
    def fullname (self):
        return self.Name

Teachers = Staff("Teacher","50",'Kiambu','Mangu')
Groundsmen = Staff("Groundsmen","10",'Kiambu','Mangu')
Cooks = Staff("Cooks","15",'Kiambu','Mangu')
Farmers = Staff("Farmers","20",'Kiambu','Mangu')

class Teachers(Staff):
    def __init__(self,Name,number,Location,school,salary,age,status):
        super().__init__(Name,number,Location,school)
        self.salary = salary
        self.age = age
        self.status =status




tch1 = Teachers("Peter",10,'Kiambu','Mangu',20000,20,'single')
tch2 = Teachers("John",2,'Kiambu','Mangu',30000,29,'married')
tch3 = Teachers("Mary",3,'Kiambu','Mangu',40000,'31','Married')


print(f' {tch1.Name} is number {tch1.number} and teaches at {tch1.school} and  he has a salary of {tch1.salary} , he is {tch1.age} and  is {tch1.status} and lives in {tch1.Location}')
print(f' {Groundsmen.Name} are  {Groundsmen.number} and they work in  {Groundsmen.school}, they live in {Groundsmen.Location}')












