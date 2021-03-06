'''
23/12/2014 - Larissa Feng

Even Fibonnaci numbers
Problem 2 of Project Euler
(https://projecteuler.net)

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
'''

# This is a relatively simple problem, to brute force, so let's try to optimize it for fun.
# We can split this problem into two parts:
#       - Generating the fibonacci sequence in an efficient way, and
#       - Pulling out the even-valued terms of the sequence and summing them.


# Let's start with the first problem: we should be efficient both in terms of space and memory.
# Sounds like a good excuse to write a generator!
def fibonnaci_generator(limit):
    last_num = 1
    current_num = 1

    while current_num < limit+1:
        yield current_num
        last_num, current_num = current_num, last_num + current_num

# Since we have a generator, we can use a list comprehension.
# This makes pulling out the even-valued terms trivial.
print sum([x for x in fibonnaci_generator(4000000) if x%2 == 0])




