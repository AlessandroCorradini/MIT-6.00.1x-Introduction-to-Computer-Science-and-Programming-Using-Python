# Write a function is_triangular that meets the specification below. 
# A triangular number is a number obtained by the continued summation 
# of integers starting from 1. For example, 1, 1+2, 1+2+3, 1+2+3+4, etc.,
#  corresponding to 1, 3, 6, 10, etc., are triangular numbers.

# def is_triangular(k):
#     """
#     k, a positive integer
#     returns True if k is triangular and False if not
#     """
#     #YOUR CODE HERE

# Paste your entire function, including the definition, in the box below. 
# Do not leave any debugging print statements.

import math

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    #YOUR CODE HERE
    x = (math.sqrt(8*k + 1) - 1) / 2
    if x - int(x) > 0: # if x is not an integer
        return False
    return True
