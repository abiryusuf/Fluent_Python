# tuple is collection of data in a single variable
# tuple can not chage the value or data 
# using parentheses 

dimensions = (200, 50)
print(dimensions[0])

print('Orginal dimensions: ')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print('\nModified dimensions: ')
for dimension in dimensions:
    print(dimension)

# try it yorself
print('orginal buffet: ')
buffet_style = ('a', 'b', 'c', 'd', 'e')
for style in buffet_style:
    print(style)

# buffet_style[0] = 'f'
# print(buffet_style)

buffet_style =('a', 'b', 'c', 'f', 'g')
print('\nReplacing two items: ')
for newItem in buffet_style:
    print(newItem)


languages = ['Python', 'C', 'C++', 'Java']
i = 0

for language in languages:
    print(i + 1, language)
    i+=1

for i, language in enumerate(languages):
    print('{} - {}'.format(i+1, language))

