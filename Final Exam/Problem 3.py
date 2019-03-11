# Implement a function that meets the specifications below.

# def sum_digits(s):
#     """ assumes s a string
#         Returns an int that is the sum of all of the digits in s.
#           If there are no digits in s it raises a ValueError exception. """
#     # Your code here
# For example, sum_digits("a;35d4") returns 12.

# Paste your entire function, including the definition, in the box below. 
# Do not leave any debugging print statements.

def sum_digits(string):
    if any(i.isdigit() for i in string):
        return sum(int(x) for x in string if x.isdigit())
    else:
        raise ValueError('No digits in input')