greeting = "Good Morning, "
name = "Sayantan"
print(type(name))

# Concatenating two strings
c = greeting + name
print(c)
name = "Sayantan"
print(name[4])
# name[3] = "d"   # --> Does not work

print(name[1:7])
print(name[:5])  # is same as name[0:5]
print(name[1:])  # is same as name[1:7]
c = name[-4:-1]  # is same is name[4:7]
print(c)
