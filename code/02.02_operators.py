a = 10
b = 7

# Arithmetic Operators
print("The addition of a and b is ", a+b)
print("The subtraction of a and b is ", a-b)
print("The multiplication of a and b is ", a*b)
print("The division of a and b is ", a/b)
print("The division result without decimal of a and b is ", a//b)
print("The decimal division result  of a and b is ", a % b)
print("The value of \"a to the power b\" is ", a**b)

# Assignment Operators
a += 12     # Shortcut of a = a+12
print("Shortcut process of a=a+12 and result is: ", a)
a -= 12     # Shortcut of a = a-12
print("Shortcut process of a=a-12 and result is: ", a)
a *= 12     # Shortcut of a = a*12
print("Shortcut process of a=a*12 and result is: ", a)
a /= 12     # Shortcut of a = a/12
print("Shortcut process of a=a/12 and result is: ", a)
a **= 12    # Shortcut of a = a**12
print("Shortcut process of a=a**12 and result is: ", a)


# Comparison Operators
b = (14 <= 7)  # Operation of "less than equal"
print(b)
b = (14 >= 7)  # Operation of "greater than equal"
print(b)
b = (14 < 7)  # Operation of "less than"
print(b)
b = (14 > 7)  # Operation of "greater than"
print(b)
b = (14 == 7)  # Operation of "equal"
print(b)
b = (14 != 7)  # Operation of "not equal"
print(b)


# Logical Operators
bool1 = True
bool2 = False
print("The value of bool1 and bool2 is", (bool1 and bool2))
print("The value of bool1 or bool2 is", (bool1 or bool2))
print("The value of not bool2 is", (not bool2))


# This is in membership operator

ab = ['Ram', 'Sham', 'Shayam']
print("Sayantan" in ab)
print("Sayantan" not in ab)
