# aline_0 = {
#     'color': 'green',
#     'point': 5
# }
# print(aline_0)

# # index 
# x = aline_0['color']
# print(x)
#  # add
# aline_0["age"] = 32
# aline_0['Place'] = "NY"
# print(aline_0)

# # change 
# aline_0['Place'] = 'Florida'
# print(aline_0)

# del aline_0['Place']
# print(aline_0)

# file_count ={}

# file_count['jpg'] = 10
# file_count['text'] = 14
# file_count['cvs'] = 2
# file_count['py'] = 33

# # modify
# x = file_count ['cvs'] = 3
# print("the cvs is now {} before it was 2, ".format(x))

alien = {
    'x_position': 0,
    'y_position': 25,
    'speed': 'medium'
}
print('Orginial x-position: ' + str(alien['x_position']))

if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien['x_position'] = alien['x_position'] + x_increment
print('New x-postion: ' + str(alien['x_position']))

# print('you just earend '  + str(new_points) +" points")

# for dic in aline_0.items():
#     print(dic)

# try it yourself
person = {
    "first_name": "Abir",
    'last_name': 'Yusuf',
    "Age": 32,
    "City": "NY"
}
print(person)
for info in person.items():
    print(info)