foods = ['pizza','falafel', 'carrot', 'cake', 'Burger']

print('my favorite foods are:')
my_foods = foods[:3]
# add new food by append method that will add end of the list
my_foods.append('cannoli')
print(my_foods)

print("\nMy friend's favorite foods are: ")
friends_food = foods[2:]
friends_food.insert(1, "ice cream")
print(friends_food)