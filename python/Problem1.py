'''
23/12/2014 - Larissa Feng

MULTIPLES OF 3 AND 5
Problem 1 of Project Euler
(https://projecteuler.net)

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

# Let's write a solution that is extensible and can easily be
# configured to deal with factors/limits other than (3,5) and 1-1000

FACTORS = (3,5)
LOWER_LIMIT = 1
UPPER_LIMIT = 1001

def sum_of_multiples(factors, lower_limit, upper_limit):
    return sum([x for x in xrange(lower_limit, upper_limit) if is_multiple(x, factors)])

def is_multiple(num, factors):
    for f in factors:
        if num % f == 0:
            return True
    return False

print sum_of_multiples(FACTORS, LOWER_LIMIT, UPPER_LIMIT)