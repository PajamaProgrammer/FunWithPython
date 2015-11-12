# Name: Pajama Programmer
# Date: 11-Nov-2015
# Program: Use Recursion to generate the first 'x' terms of the fibonacci sequence 

"""
The fibonacci sequence is a series of integers such that 1 1 2 3 5 8 13...
Where each subsequent number is the summation of the previous two
"""

def fibonacci_sequence (x):
    if x < 2: return (0, 1) #Base Case
    else:
        fib_seq = fibonacci_sequence(x-1) 
        fib_seq += (fib_seq[x-1]+fib_seq[x-2],)
        return fib_seq
    

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.
if __name__ == '__main__':        
    fib = fibonacci_sequence (12)

    print(fib)
