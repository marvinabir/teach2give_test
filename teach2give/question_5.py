#Question 5: Reverse Integer
#Write a program that takes an integer as input and returns an integer with reversed digit ordering.

def reverse_int(num):
    if num < 0:
        return -int(str(-num)[::-1])
    else:
        return int(str(num)[::-1])

# Example 
print(reverse_int(500))  
print(reverse_int(-56))  
print(reverse_int(-90))  
print(reverse_int(91))   
