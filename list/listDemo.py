bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles[0].title())

print(bicycles[-2].title())

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

# bicycles.pop(1)
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

# print(sorted(cars))
# Range 
# thisList = ["apple", "banana", "cherry", "orange", "melon", "mango"]

# y = thisList[1:3]

# print(y)

# t = "apple" in thisList
# print(t)

# List compreshensions
# multiples = []
# for x in range(1, 11):
#     if x % 2 == 0:
#         multiples.append(x * 2)
# print('EVEN {}'.format(multiples))

# z = [x * 2 for x in range(1,20+1) if x % 2 == 0]
# print("Even: {}".format(z))

# Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
# name = ['Abir', 'Usan', 'Mim', 'Arju']
# for i, person in enumerate(name):
#     print("{} - {}".format(i+1, person))

def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n])
	return("")
print(get_word('I am abir', 1))