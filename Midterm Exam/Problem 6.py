# Write a function that satisfies the following docstring:

# def largest_odd_times(L):
#     """ Assumes L is a non-empty list of ints
#         Returns the largest element of L that occurs an odd number 
#         of times in L. If no such element exists, returns None """
#     # Your code here
# For example, if

# largest_odd_times([2,2,4,4]) returns None
# largest_odd_times([3,9,5,3,5,3]) returns 9
# Paste your entire function, including the definition, in the box below. 
# Do not leave any debugging print statements.

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    if len(L) == 0:
        return None
    
    value = max(L)
    
    if L.count(value) % 2 != 0:
        return value
    else:      
        return largest_odd_times(list(filter(lambda a: a != value, L)))
  
        
    