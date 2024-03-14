# my_tuple = (10, 20, 30, 40, 50)
# print(my_tuple)
# print(my_tuple[3])
# print(my_tuple[3:5])
# print(len(my_tuple))
# del my_tuple
# print(my_tuple)
my_tuple2 = (11, 22, 30, 44, 30)
print(my_tuple2)
print(my_tuple2.count(30))
print(max(my_tuple2))
print(min(my_tuple2))
print(sum(my_tuple2))
print(sum(my_tuple2)/len(my_tuple2))
print(my_tuple2.index(44))
if 22 in my_tuple2:
    print("22 is in my_tuple2")
else:
    print("22 is not in my_tuple2")
