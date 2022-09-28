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