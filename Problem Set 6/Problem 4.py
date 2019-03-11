# Consider the following Python procedure. Specify its order of growth.

def modten(n):
    return n%10

# O(1)

# Consider the following Python procedure. Specify its order of growth.

def multlist(m, n):
    '''
    m is the multiplication factor
    n is a list.
    '''
    result = []
    for i in range(len(n)):
        result.append(m*n[i])
    return result

O(len(n))

# Consider the following Python procedure. Specify its order of growth.

def foo(n):
    if n <= 1:
        return 1
    return foo(n/2) + 1

# Consider the following Python procedure. Specify its order of growth.

def recur(n):
    if n <= 0:
        return 1
    else:
        return n*recur(n-1)

O(n)

# Consider the following Python procedure. Specify its order of growth.

def baz(n):
    for i in range(n):
        for j in range(n):
            print i,j

O(n^2)