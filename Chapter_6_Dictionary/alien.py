aline_0 = {
    'color': 'green',
    'point': 5
}
print(aline_0)

# index 
x = aline_0['color']
print(x)
 # add
aline_0["age"] = 32
aline_0['Place'] = "NY"
print(aline_0)

# change 
aline_0['Place'] = 'Florida'
print(aline_0)

del aline_0['Place']
print(aline_0)




new_points = aline_0['point']
print('you just earend '  + str(new_points) +" points")

for dic in aline_0.items():
    print(dic)