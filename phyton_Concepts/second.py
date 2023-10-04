# List Comprehension + Dict/Set Comprehension

lis = [expression for i in iterable if condition]

l1 = [i for i in range(1,4)]              # [1,2,3]

l2 = [i*2 for i in range(1,4)]            # [2,4,6]

l3 = [i**2 for i in range(1,4)]           # [1,4,9]

l4 = [i for i in range(1,4) if i%2==1]    # [1,3]

# ^ with list comprehension, we can create a custom list in one line of code.

set1 = {i for i in range(1,4)}          # {1,2,3}

d1 = {i:i**2 for i in range(1,4)}       # {1:1, 2:4, 3:9}

# ^ set comprehension and dictionary comprehension can be used to create sets and dictionaries in the same way we create lists using list comprehensions.