'''Question 1
Given two strings s and t, determine whether some anagram of t is a substring of s. 
For example: if s = "udacity" and t = "ad", then the function returns True. 
Your function definition should look like: question1(s, t) and return a boolean True or False.'''

# Need to break s into single characters
# Check whether t is made up of only those characters in any order but no duplicates.
# Return true if it is

# time comlexity == O(n)
from collections import Counter

def question1(s,t):
    if s is None or t is None: # check for null inputs
        print "Looking for '" + str(t) + "' in '" + str(s) + "': "
        return "Inputs cannot be null."
    elif s != str(s) or t != str(t): # inputs must be strings
        print "Looking for '" + str(t) + "' in '" + str(s) + "': "
        return "Inputs must be strings containing only letters."
    elif len(s) == 0 or len(t) == 0 or len(t) >= len(s): # 's' must be longer than 't'. Inputs can't be empty.
        print "Looking for '" + t + "' in '" + s + "': "
        return "Inputs cannot be empty. 's' must be longer than 't'."
    s,t = s.lower(), t.lower() # correct for upper + lower case letters
    t_dict = Counter(t) # create dictionary of letters in 't'
    for i in range(len(s) - len(t) + 1): # loop over 's' to find all possible substrings of len(t)
        s_slice = Counter(s[i:i+len(t)]) # convert 's' substring to dict to compare it to 't_dict'
        if s_slice == t_dict: # True if one of the 's_slice' equals 't_dict'
            print "Looking for '" + t + "' in '" + s + "': "
            return True
    print "Looking for '" + t + "' in '" + s + "': "
    return False


print "*** Question 1 ***"
print ""
print question1('udacity', 'ad') 
# Answer: True
print question1('dormitory', 'room') 
# Answer: False
print question1('astronomy', 'moony') 
# Answer: True
print question1('bubble','sort') 
# Answer: False
print question1('bubble','bub') 
# Answer: True

# ***Edge Cases***
print question1('udaCiTy', 'cIty') # Edge Case: upper and lower-case letters
# Answer: True
print question1('bubble','') # Edge Case: Empty string
# Answer: Inputs cannot be empty. 's' must be longer than 't'.
print question1('bubble', None) # Edge Case: Null input
# Answer: Inputs cannot be null.
print question1(1,'abc') # Edge Case: Integer input
# Answer: Inputs must be strings containing only letters.
print question1('abc','cba') # Edge Case: 's' and 't' are the same length.
# Answer: Inputs must be strings containing only letters.
print ""







