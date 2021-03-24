foods = ['pizza','falafel', 'carrot', 'cake', 'Burger']

print('my favorite foods are:')
my_foods = foods[:3]
# add new food by append method that will add end of the list
my_foods.append('cannoli')
print(my_foods)

print("\nMy friend's favorite foods are: ")
friends_food = foods[2:]
# add new item by insert method that will add with index number
friends_food.insert(1, "ice cream")
print(friends_food)

# try it yourself 
languages = ['java', 'python', 'C++', 'javaScript', 'C', 'ruby']

print(languages[:3])

print(languages[2:4])

print(languages[3:])


pizza = ['ab', 'cc', 'dd', 'ee']

friend_pizza = pizza[1:3]
print(friend_pizza)
friend_pizza.append('ff')
print(friend_pizza)


print("My favorite pizza are:")
for myPizza in pizza:
    print('- ' + myPizza)

print("\n My friend's favorite pizza are: ")
for myFriendPizza in friend_pizza:
    print('_ ' + myFriendPizza)
