
for value in range(1, 5 +1):
    print(value)
# def myFun(n):
#     for x in range(1,n -1):
#         print(x)

# myFun(6)
for x in list(range(1,5)):
    print(x)
print(type(x))

# even number 
# even_number = list(range(2,11,2))
# print(even_number)

# square

squares = []

for value in range(1,11):
    squre = value * 2
    squares.append(squre)
print(squares)

def function(n):
    squares = []
    for value in range(1, n +1):
        squares.append(value *2)
    return squares
print(function(6))