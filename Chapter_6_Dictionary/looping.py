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