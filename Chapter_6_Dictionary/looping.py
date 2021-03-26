languages = {
    'abir': "python",
    "mim": 'java',
    'sarah': 'c',
    'yusuf': 'ruby',
    'phil': 'c++'
}
for name, language in languages.items():
    print("{}'s favorite language is {}".format(name.title(), language.title()))

x = languages['abir'].title()
print(x)

friends = ['phil', 'sarah']

for name in languages.keys():
    print(name)
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + languages[name].title())


# sorted
for name in sorted(languages.keys()):
    print(name.title() + ", thank for taking the poll")

# values
for language in sorted(languages.values()):
    print(language.title())

for name, language in sorted(languages.items()):
    print("{}'s likes {}".format(name.title(), language.title()))


for language in set(languages.values()):
    print(language)


# try it yourself
rivers = {
    'bangladesh': 'karnafuly',
    'new york': "hudson",
    'canada': 'abc'
}

for name, river in rivers.items():
    print("The {} runs through {}.".format(name.title(), river.title()))

for name in rivers.keys():
    print("Country: " + name.title())

for value in rivers.values():
    print(value.title())

peoples = ['abir', 'mim', 'mukter', 'arafat']

for people in peoples:
    if people in languages.keys():
        print('Thank you for taking the poll, ' + people.title())
    else:
        print(people.title() + ' whats your favorite langiages')