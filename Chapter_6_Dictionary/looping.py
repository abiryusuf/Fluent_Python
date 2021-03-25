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