#Tuple Unpacking + Tuple Unpacking With *

person = ['bob', 30, 'male']

name, age, gender = person

# name='bob, age=30, gender='male'

# ^ we can use tuple unpacking to assign multiple variables at one go.

fruits = ['apple', 'orange', 'pear', 'pineapple', 'durian', 'banana']

first, second, *others = fruits

# first='apple', second='orange'
# others = ['pear', 'pineapple', 'durian', 'banana']

# ^ we can add * in front of variables to unpack everything else into that variable.