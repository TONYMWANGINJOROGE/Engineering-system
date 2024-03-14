def hello_world():
    print('hello_world')
    print('hello_world')
    print('hello_world')
hello_world()
def nyumba(name):
    print(name)
    print(name)
    print(name)
nyumba('Tony')
nyumba('peter')

def num(nambari):
    print(nambari)
    print(nambari)
    print(nambari)
num(30)

num(nambari='Tony')
def num1 (fname):
    print(fname+'is my favorite number')
num1('Tony')

def students(first_name,last_name):
    print(first_name+last_name + 'please enter your name')
students('Tony','Mwangi')

def employees(first_name,Age):
    if int (Age)<20:
        print(first_name + 'you are below 20 years old')
    elif int(Age)<=30:
        print(first_name + 'you are middle aged')
    else:
        print(first_name + 'you are older than 30')
employees('Tony ','20')
employees('peter ','50')

def age_calculator(age):
    new_age = age +10
    return new_age
calculated_age = age_calculator(40)
print(calculated_age)

def age_calculator(age):
    new_age = age -7
    return new_age
age_calculator(30)
print(age_calculator(30))

def perfomance_calculator(eng,kisw,math):
    total = eng + kisw + math
    return total
perfomance = perfomance_calculator(eng=100,kisw=70,math=90)
print(perfomance)

def perfomance_calculator(*subjects):
    total=sum(subjects)
    return total
perfomance = perfomance_calculator(23,24)
print(perfomance)

def country(nchi = 'ivory Coast'):
    return nchi
print(country('Jamaica'))
print(country('colombia'))
print(country('britain'))
print(country())

def ongeza(x):
    return x*x
ongeza = ongeza(11)
print(ongeza)