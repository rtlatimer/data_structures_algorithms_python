'''Question 1
Given two strings s and t, determine whether some anagram of t is a substring of s. 
For example: if s = "udacity" and t = "ad", then the function returns True. 
Your function definition should look like: question1(s, t) and return a boolean True or False.'''

# Need to break s into single characters
# Check whether t is made up of only those characters in any order but no duplicates.
# Return true if it is


from collections import Counter

def question1(s,t):
    if s and t: # Check to see if string is empty
        if len(s) >= len(t): # 't' should not be longer than 's'
            for char in range(len(s)):
                if Counter(t.lower()) == Counter(s.lower()[char:char + len(t)]):
                    print "Looking for '" + t + "' in '" + s + "': "
                    return True
    print "Looking for '" + t + "' in '" + s + "': "
    return False

print question1('udacity', 'ad') # True
print question1('udaCiTy', 'city') # True
print question1('dormitory', 'room') # False
print question1('astronomy', 'moony') # True
print question1('bubble','sort') # False
print question1('bubble','') # False
print question1('bubble','bub') # True
print question1('spongebob', 'bboeg') # True



