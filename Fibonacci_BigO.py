# Name: Pajama Programmer
# Date: 10-Feb-2016
# Program: Variouse Methods of Solving for the Nth term of the Fibonacci Sequence
# The goal is the study the time complexities of the different implementations
# 
# For more information see,
# https://www.youtube.com/watch?v=L4Rgq8J7ZzA - Matrix Equations and Fibonacci
# https://www.youtube.com/watch?v=ewd7Lf2dr5Q - MIT 6.00 Big O notation

from math import sqrt
import time

"""
Solving for the nth term using Matrix multiplication.
"""
#O(1)
def matrix_mult(A, B):
    """
    A and B are 2x2 matrices
    returns the result of AxB
    """
    return ([A[0][0] * B[0][0] + A[0][1] * B[1][0],
             A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0],
             A[1][0] * B[0][1] + A[1][1] * B[1][1]])

#O(log n)
def matrix_exp(A, e):
    """
    A is a 2x2 matrix
    e is the exponent
    returns the result of A^e

    A^0 = Identity Matrix

    This function is able to achieve O(log n) because of this simple property
    of exponentials: x^y = (x*x)^(y/2) assuming y is an even number    
    """
    if e == 0:          #return Identity Matrix
        return [[1,0],
                [0,1]]
    elif e%2 == 0:      
        return matrix_exp(matrix_mult(A, A), e//2)
    else:
        return matrix_mult(A, matrix_exp(A, e-1))

#O(log n)                         
def fib_matrix(n):
    """
    Using matrix equations to solve for the nth term.
    The time complexity can be found in the following manner:
    T1(n) = 3 + T2(n), T2(n) is the time for matrix_exp function
    T2(n) = 2 + T2(n/2), when n is even
    T2(n) = 2 + T2(n-1), when n is odd, however, on next iteration n is even...
    T2(n) = 4 + T2(n/2) = 4 + 4 + T2(n/4) = .... = 4k + T2(n/2^k)
    base case is 2^k = n, k = log n

    T1(n) = 4log n + T2(1) = O(log n)...
    """
    if n < 0:
        raise Exception("negative number")
    if n in [0,1]:
        return n
    M = [[0,1],[1,1]]
    return matrix_exp(M,n)[0][1]

"""
Solving for the nth term using the binet formula.
Binet Formula: Fn = (1/sqrt(5))*[T1^n - T2^n],
where T1 = (1+sqrt(5))/2 and T2 = (1-sqrt(5))/2
"""
#O(log n)
def pow(base, exp):
    """
    Helper function, simply caculates base to the power of exp (base^exp)
    This function is able to achieve O(log n) because of this simple property
    of exponentials: x^y = (x*x)^(y/2) assuming y is an even number  
    """
    if exp == 1:
        return base
    elif exp%2 == 0:
        return pow(base*base, exp//2)
    else:
        return base*pow(base, exp-1)

#O(log n)
def fib_binet(n):
    """
    Using the Binet Formula to solve for the nth term.
    Binet Formula: Fn = (1/sqrt(5))*[T1^n - T2^n],
    where T1 = (1+sqrt(5))/2 and T2 = (1-sqrt(5))/2

    T(n) = 6 + 2*T1(n), where T1 is the time of pow function
    T1(n) = 4 + T1(n/2), applying worst case for even/odd
    T1(n) = 4 + 4 + T1(n/4) = 4 + 4 + 4 + T1(n/8) = 4k + T1(n/2^k)
    base case with n/2^k = 1, or 2^k = n, or k = log n

    T(n) = 6 + 2*(4log n + T1(1)) = O(log n)
    """
    if n < 0:
        raise Exception("negative number")
    if n in [0,1]:
        return n

    t1 = (1+sqrt(5))/2
    t2 = (1-sqrt(5))/2
    x = 1/sqrt(5)

    fibn = x*(pow(t1, n) - pow(t2, n))
    return fibn

"""
Fibonacci, solving for nth term using recursion
"""
#O(2^n)
def fib_recursive(n):
    """
    The time complexity of this method is outrageous!
    T(n) = 2 + T(n-1) + T(n-2), will set T(n-1) = T(n-2) just for ease...
    T(n) = 2 + 2*T(n-1) = 2 + 2*2 + 2*2T(n-2) = 2 + 2*2 + 2*2*2 + 2*2*2T(n-3)
    T(n) = 2 + 2^2 + 2^3 + ... + 2^k + 2^kT(n-k), until n-k=0 or k=n
    O(2^n)
    """
    if n < 0:
        raise Exception("negative number")
    if n in [0,1]:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

"""
Fibonacci, solving for nth term using a memo and recursion
"""
memo = {0:0, 1:1, 2:1}
#O(n)
def fib_memo(n):
    """
    This drops the complexity to O(n)
    T(n) = 2 + T(n-1) + 1, last term equates to 1 because T(n-2) will be in the memo
    T(n) = 3 + 3 + T(n-2) = 3k + T(n-k), until k=n in the worst case
    """
    if n < 0:
        raise Exception("negative number")
    if n in memo:      #Check if nth term has been found
        return memo[n]

    memo[n] = fib_memo(n-1) + fib_memo(n-2)    #find nth term and assign to memo
    return memo[n]

"""
Fibonacci, solving for nth term using iteration
"""
#O(n)
def fib_iter(n):
    """
    O(2 + n*2) = O(n)
    """
    if n < 0:
        raise Exception("negative number")

    a, b = 0, 1
    for i in range (n):
        nextTerm = a+b
        a = b
        b = nextTerm

    return a

"""
Testing the Methods
"""
def test_fib(n = 10, fib_funct = fib_iter, total_time = True, display = False, do_range = False):
    fib_num = -1
    start_time = time.time()
    if do_range:
        for i in range (n):
            fib_num = fib_funct(i)
            if display:
                print(fib_num)     
    else:
        fib_num = fib_funct(n)
        if display:
            print(fib_num)
        
    end_time = time.time()

    fib_time = end_time - start_time
    
    if total_time:
        print("Total Time:", end_time-start_time)
 
    return [fib_time, fib_num]
    
        

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.
if __name__ == '__main__':   

    N = 1000000
    n = 0
    fib_binet_time = 0
    fib_memo_time = 0
    fib_matrix_time = 0
    fib_iter_time = 0
    fib_recur_time = 0
    total_time = False
    display = True
    do_range = False

    while (n < N):
        fib_binet_time += test_fib(n, fib_binet, total_time, display,)[0]
        fib_memo_time += test_fib(n, fib_memo, total_time, display, do_range)[0]
        fib_matrix_time += test_fib(n, fib_matrix, total_time, display,)[0]
        fib_iter_time += test_fib(n, fib_iter, total_time, display,)[0]
        if (n < 45):
            fib_recur_time += test_fib(n, fib_recursive, total_time, display,)[0]
        
        print("Nth Term:", n)
        print("Binet Formula:\t\t", fib_binet_time)
        print("Memo Formula:\t\t", fib_memo_time)
        print("Matrix Formula:\t\t", fib_matrix_time)
        print("Iteration Formula:\t", fib_iter_time)
        print("Recursive Formula:\t", fib_recur_time)

        if n < 100:
            n += 10
            if n > 50:
                display = False
                
        else:
            n *= 10
            do_range = True #prevent recusion error in fib_memo
            
            
