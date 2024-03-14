weight = float(input("Enter the weight in Kg: "))
if weight < 0:
    print("invalid weight")
height = float(input("Enter the height in m: "))
if height < 0:
    print("invalid height")
BMI = (weight/(height*2))
print("Your BMI is")
print(BMI)
if BMI < 0:
    print("invalid BMI")
elif BMI < 18:
    print('underweight')
elif BMI>=18 and BMI<=24:
    print('normal')
elif BMI > 24 and BMI < 30:
    print('overweight')
elif BMI > 30:
    print('obese')
else:
   print('invalid')