'''Question 2
Given a string a, find the longest palindromic substring contained in a. 
Your function definition should look like question2(a), and return a string.'''

# Similar to Project Euler problem where looked at list of numbers
# Take a and see if any portion of it is palindromic.
# Return the longest palindromic portion

def question2(a):
    if len(a) > 2:
        string = a.lower()
        word = string[0]
        for char in range(len(string)):
            for char2 in range(0, char):
                sub = string[char2:char + 1]
                if sub == sub[::-1]:
                    if len(sub) > len(word):
                        word = sub
        if len(word) > 1:
            return word
        else:
            return None
    return None
    

print question2('bub')
print question2('canals')
print question2('amanaplanacanalpanamabanana')
print question2('')
print question2('robert')
print question2('udacity')
print question2('rubberband')
print question2('kAyaks')