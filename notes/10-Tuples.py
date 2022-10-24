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


