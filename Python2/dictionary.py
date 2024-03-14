# my_dictionary= {
#
#     'Name':'Tony'
# }
# my_dictionary={
#     'Name':'Tony',
#     'Age': 20,
#     'Gender':'Male',
#     'Status':'single'
# }
# print(my_dictionary)
# print(my_dictionary['Gender'])
# print(my_dictionary.get('Name'))
# my_dictionary['status']='complicated'
# print(my_dictionary)
# my_dictionary['Birthdate']=2000
# print(my_dictionary)
# my_dictionary['school']='kabianga'
# print(my_dictionary)
# my_dictionary2= my_dictionary.copy()
# print(my_dictionary2)
# print(len(my_dictionary))
# my_dictionary.pop('status')
# print(my_dictionary)
# # del my_dictionary['Name']
# # print(my_dictionary)
# # my_dictionary.clear()
# # print(my_dictionary)
# if 'Name'in my_dictionary:
#     print('Name found in dictionary')
# else:
#     print('Name not found in dictionary')
# for value in my_dictionary:
#     print(my_dictionary[value])
#     for key in my_dictionary:
#         print(my_dictionary[key])
#
#         for key,value in my_dictionary.items():
#             print(key,value)
my_dictionary={
    'soap':50,
    'toothpaste':200,
    'cake':500,
    'trouser':1000,
    'shirt':2500
}
print(my_dictionary)
if 'cake'in my_dictionary:
    print('cake found in dictionary')
else:
    print('cake not found in dictionary')
print(my_dictionary['cake'])
my_dictionary['bread']=150
print(my_dictionary)