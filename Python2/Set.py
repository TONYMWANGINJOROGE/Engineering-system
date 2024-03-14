my_set = {100,200,300,400,500}
print(my_set)
var1 = 300
if var1 in my_set:
    print(var1)
var2 = 400
if var2 in my_set:
    print(var2)
my_set.add(700)
print(my_set)
# my_set.update([305,405,505])
# my_set2 = my_set.copy([305,405,505])
print(len(my_set))
print(max(my_set))
print(min(my_set))
print(my_set)
print(max(my_set)/min(my_set))
my_set.discard(300)
my_set.clear()
print(my_set)
if 32 in my_set:
    print('32 in my_set')
else:
    print('not found')
    print(my_set)