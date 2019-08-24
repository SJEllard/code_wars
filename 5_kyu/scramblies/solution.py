from collections import Counter

#Counter similar to a predefined dictionary operation, 
#counts letters in string (See more in ipynb)
#The operator "not" yields True if its argument is false, False otherwise.
def scramble(s1, s2):
    count_1 = Counter(s1)
    count_2 = Counter(s2)
    return not(Counter(s2) - Counter(s1))