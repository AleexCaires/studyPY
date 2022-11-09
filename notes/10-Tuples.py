# Tuples are another kind of sequence, like a list. They have elements which are indexed starting at 0.

# Tuples are immutable (similar to strings)

# A few things that can't be done with tuples 
# sort(); append();reverse();

# Tuples are more efficient 

# Since they can't be modifiable, they are simpler and more efficient in terms of memory and performance than lists.

# To make "temporary variables" we prefer tuples over lists.

# We can put tuples on the left hand side of an assignment statement.
(x,y)  = (4, 'fred')
print(y)

# The items() method in dictionaries return a list of (key, value) -> tuples

# Tuples are comparable

(0,1,2) < (5,1,2)
#true


#10 - Tuples B 
#Sorting List of Tuples

#- We can take advantage of the ability to sort a list of tuples to get a sorted list of a dictionary
# First we sort the dictionary by the key using the items() method and sorted() function


#Sorting by Values instead of key

#If we could construct a list of tuples of the form(value,key) we could sort by value.
#We do this with a for loop that creates a list of tuples
#Example:

c={'a': 10, 'b':1,'c':22}
temp = list()
for k,v in c.items():
    temp.append((v,k))

    
