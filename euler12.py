# What is the value of the first triangle number to have over five hundred divisors?
# The sum of first n natural numbers or the nth triangular number is given by n*(n+1)/2
# Answer :76576500


from functools import reduce
import time


# function to check for divisors
def divisors(trinum):
    expList = []
    ctr = 0
    divisor = 2
    while divisor <= trinum:
        while trinum % divisor == 0:
            trinum = trinum / divisor
            ctr += 1
        if ctr != 0:
            expList.append(ctr + 1)
        divisor += 1
        ctr = 0
    return reduce(lambda trinum, y: trinum * y, expList, 1)


# function to generate triangular number
def tri_num(n):
    natural = 1
    triangular_num = 0

    while True:
        triangular_num += natural
        natural += 1
        if divisors(triangular_num) > n:
            break
    return triangular_num


# main program
if __name__ == "__main__":
    # Time at the start of program execution
    start_time = time.time()
    print(tri_num(500))
    # print(n_divisors(500))
    # Time at the end of program execution
    end_time = time.time()
    # Printing the time of execution
    print(end_time - start_time)
