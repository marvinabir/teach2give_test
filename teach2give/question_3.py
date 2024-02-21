#Question 3: Power of Two
#Write a program that takes an integer as input and returns true if the input is a power of two.

def power_of_two(x):
    
    return x > 0 and (x & (x - 1)) == 0

#example 
print(power_of_two(8))  
print(power_of_two(6))  
