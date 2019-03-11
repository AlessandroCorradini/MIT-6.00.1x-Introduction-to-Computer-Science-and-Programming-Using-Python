# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters 
# occur in alphabetical order. For example, if s = 'azcbobobegghakl', 
# then your program should print

# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd', 
# then your program should print

# Longest substring in alphabetical order is: abc

# Note: This problem may be challenging. We encourage you to work smart. 
# If you'\ve spent more than a few hours on this problem, we suggest 
# that you move on to a different part of the course. If you have time, 
# come back to this problem after you've had a break and cleared your head.

# Paste your code into this box 

maxLen=0
current=s[0]
longest=s[0]

# step through s indices
for i in range(len(s) - 1):
    if s[i + 1] >= s[i]:
        current += s[i + 1]
        # if current length is bigger update
        if len(current) > maxLen:
            maxLen = len(current)
            longest = current
    else:
        current=s[i + 1]
        
    i += 1

print ('Longest substring in alphabetical order is: ' + longest)
