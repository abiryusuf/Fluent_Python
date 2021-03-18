# bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# print(bicycles[0].title())

# message = "My first bicyle was a " + bicycles[0].title() + "."
# print(message)

# for x in bicycles:
#     print(x[0].title() + x[1].title())


# bicycles.append("car")
# print(bicycles[-1].title())

# bicycles.insert(2, "honda")
# print(bicycles)

# bicycles[2] = 'toyota'
# print(bicycles)

# del bicycles[0]
# print(bicycles)

# bicycles.append("trek")
# print(bicycles)

# bicycles.pop(0)
# print(bicycles)

# too_expensive = 'honda'
# bicycles.remove(too_expensive)
# print(too_expensive)
# print("\nA " + too_expensive.title() + ' is too expensive for me. ')

# sort 
# maintain the order based on the letter
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)

# cars.sort(reverse=True)
# print(cars)

# Range 
# thisList = ["apple", "banana", "cherry", "orange", "melon", "mango"]

# y = thisList[1:3]

# print(y)

# t = "apple" in thisList
# print(t)

# List compreshensions

z = [x * 2 for x in range(1, 20) if x % 2 == 0]
print("Even {}" .format(z))