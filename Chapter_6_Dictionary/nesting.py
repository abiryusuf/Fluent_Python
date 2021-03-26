alien_0 = {'color': 'green', 'points': 5} 
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_2, alien_1, alien_0]

for alien in aliens:
    print(alien)

aliens_Empty = []
for alien in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens_Empty.append(new_alien)

for alien in aliens[:5]:
    print("number" + str(alien))
