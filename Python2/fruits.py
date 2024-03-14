class Fruits:
    def __init__(self, name, color,price):
        self.name = name
        self.color = color
        self.price = price
    def __str__(self):
        return f'My best fruit is {self.name} because it is {self.color} and it costs {self.price}'

f1=Fruits('apple','green','30$')
f2=Fruits('pawpaw','yellow','70$')
f3=Fruits('banana','yellow','10$')
f4=Fruits('orange','orange','20$')
f5=Fruits('kiwi', 'green','50$')

print(f1)
print(f2)
print(f3)
print(f4)
print(f5)


