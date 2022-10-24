# What is a collection (in memory data base) it's a situation where we have a variable, like a list or a dictionarie and we can put multiple pieces of information.

# Dictionaries are like lists except that they use keys instead of numbers to look up values.

# Dictionaries literals(constants) -> they use {}

# 09 - Dictionaries B 

# One common thing of Dictionaries is counting how often we "see" something

counts = dict()
names=['Alex','Tiago','Gomes','Caires']
for name in names:
    if name not in counts:
        counts[name] = 1
    else: 
        counts[name]= counts[name]+1
print(counts)

# The get method for dictionaries

counts = dict()
names=['alex','caires','tiago']
for name in names:
    counts[name] = counts.get(name,0) + 1
print(counts)