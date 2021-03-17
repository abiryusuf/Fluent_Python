bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles[0].title())

message = "My first bicyle was a " + bicycles[0].title() + "."
print(message)

for x in bicycles:
    print(x[0].title() + x[1].title())


bicycles.append("car")
print(bicycles[-1].title())