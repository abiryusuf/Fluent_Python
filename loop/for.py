# for c in range(5):
#     print("execute from 0 to 4 = " + str(c))

# for x in range(5):
#     print("execute from 1 to 5 = " + str(x +1))

color = ['red','black', 'green']

# for t in color:
#     print(t)

# r = color[0]
# print(r)
# for d in r:
#     print(d)

# for y in "Abir":
#     print("String the loop " + str(y))


# Break
# for x in color:
#     if x == "black":
#         break
#     print("Break " + str(x))

# for c in color:
#     if c == "black":
#         continue
#     print("Continue: " + str(c))
# specify the starting the value
# for a in range(2, 8):
#     print(a)

# for x in range(1,10,2):
#     print(x)

# else
# for x in range(1,8):
#     if x == 5:
#         continue
#     print(x)
# else:
#     print("Finished")

# def sum_squares(n):
#     sum = 0
#     for c in range(n):
#         sum += c * c
#     return sum
# print(sum_squares(10))

# total and find the length

num = [4, 6, 7, 8]

sum1 = 0
lenght = 0
for value in num:
    sum1 += value
    lenght += 1
print("Total sum: " + str(sum1) + " - Average: " + str(sum1/lenght))

animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
char = 0
for animal in animals:
    char += len(animal)
print("Total characters: {}, Average length: {}".format(char, char/len(animal)))


def factorial(n):
    result = 1
    for x in range(1, n + 1):
        result = result * x
    return result

print(factorial(5))