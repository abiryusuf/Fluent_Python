
# for value in range(1, 5 +1):
#     print(value)
# def myFun(n):
#     for x in range(1,n -1):
#         print(x)

# myFun(6)
# for x in list(range(1,5)):
#     print(x)
# print(type(x))

# even number 
# even_number = list(range(2,11,2))
# print(even_number)

# square

# squares = []

# for value in range(1,11):
#     squre = value * 2
#     squares.append(squre)
# print(squares)

# def function(n):
#     squares = []
#     for value in range(1, n +1):
#         squares.append(value *2)
#     return squares
# print(function(6))

# # Simple statistcs with a list of numbers

# num = [2,4,6,7,8,9]

# res = (min(num))
# print("Min number: {}".format(res))

# maxNum = (max(num))
# print('Max number: ' + str(maxNum))

# total = sum(num)
# print('Total - {}'.format(total))

# # A list comprehension allows you to generate this same list in just one line of code

# squares = [value * 2 for value in range(1,11)]
# print(squares)

# for c in range(1, 21):
#     if c == 4:
#         break
#     print(c)


# try yourself
numbers = list(range(1, 1000001))

minNum = (min(numbers))

# maxNum = (max(numbers))
# print(maxNum)

# num = list(range(1,20,2))
# print(num)

# number = []

# for value in range(3,31,3):
#     number.append(value)
#     print(value)

cubes = []

for value in range(1,11):
    cube = value ** 3
    cubes.append(cube)
print(cubes)

for c in cubes:
    print(c)

cube = [value ** 3 for value in range(1,11)]
# print(cube)

for x in cube:
    print(x)

# Looping through a slice 

names = ['Abir', 'Yusuf', 'Mim', 'Madiha']

print('Here are the first three names on my list')

for name in names[:3]:
    print(name)

total = (sum(numbers))
print('Total: ' + str(total))