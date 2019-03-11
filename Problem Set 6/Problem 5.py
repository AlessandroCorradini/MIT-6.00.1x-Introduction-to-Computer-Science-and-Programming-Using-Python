# In lecture, we saw a version of linear search that used the fact that a set of
# elements is sorted in increasing order. Here is the code from lecture:

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
# Consider the following code, which is an alternative version of search.

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

# Which of the following statements is correct? You may assume that each
# function is tested with a list L whose elements are sorted in increasing
# order; for simplicity, assume L is a list of positive integers.

# search and newsearch return the same answers for all L and e.
# search and newsearch return the same answers provided L is non-empty.
# search and newsearch return the same answers provided L is non-empty and e is in L.
# search and newsearch never return the same answers.
# search and newsearch return the same answers for lists L of length 0, 1, or 2. [X]