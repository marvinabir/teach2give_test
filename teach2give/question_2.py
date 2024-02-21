#Question 2: Fibonacci Sequence
#Write a program to generate the Fibonacci sequence up to 100.

def gen_fibseq():
    fib_seq = [0, 1]  
    while True:
        next_fib = fib_seq[-1] + fib_seq[-2]  
        if next_fib <= 100:  
            fib_seq.append(next_fib)  
        else:
            break  
    return fib_seq

print( gen_fibseq())