# Intermediate Expressions

# Ex 2
name = input("Enter your name: ")
print("Hello", name)

# Ex 3

hour = input("Enter your Work Hours: ")
rate = input("Enter your rate: ")
pay = float(hour) * float(rate)

print(pay)

# Ex 6

def computepay() :
    Hours = input("Enter hours:")
    
    H = float(Hours)
    if H > 40 :
        H = (H - 40) * 1.5 + 40
    else :
        H = H
    Rate = input("Enter rate:")
    R = float(Rate)
    Payment = H * R 
    print("Payment:", Payment) 

computepay()

#Find the largest Number

largest_number = -1

for the_num in [9,41,32,69,79,1,3,89] :
    if the_num > largest_number :
        largest_number = the_num
    print(largest_number, the_num)



#Code to find the smallest value from a list of values

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)