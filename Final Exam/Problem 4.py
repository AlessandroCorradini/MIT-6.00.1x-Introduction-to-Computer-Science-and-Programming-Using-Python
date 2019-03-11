# Implement a function that meets the specifications below.

# def max_val(t): 
#     """ t, tuple or list
#         Each element of t is either an int, a tuple, or a list
#         No tuple or list is empty
#         Returns the maximum int in t or (recursively) in an element of t """ 
#     # Your code here
# For example,

# max_val((5, (1,2), [[1],[2]])) returns 5.
# max_val((5, (1,2), [[1],[9]])) returns 9.

# Paste your entire function, including the definition, in the box below. Do not leave any 
# debugging print statements.

def max_val(t):
    """ t, tuple 
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
  maxValue = 0
  mv = 0
  for item in t:
    if type(item) == list or type(item) == tuple:
        mv = max_val(item)
    else:
      if item > maxValue:
        maxValue = item
    if mv > maxValue:
      maxValue = mv
  return maxValue

