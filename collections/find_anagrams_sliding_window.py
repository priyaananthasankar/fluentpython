# Given a string s and p, return the start indices in s
# where p's anagrams are present
# s = "abcdaebcai", p = "abc"
# Return [0,6] = the start indices where abc's anagrams are present
from find_anagrams import find_anagrams

def allletterssame(p):
    anchor = p[0]
    mybool = True
    for i in p:
        if i != anchor:
            mybool = False
    return mybool
        
def return_indices(s,p):   
    set_of_anagrams = []
    if (allletterssame(p)):
        set_of_anagrams.append(p)
    else:
        find_anagrams(p,"",set_of_anagrams)
    indices = []
    i = 0 
    j = i+1
    window_size = len(p)-1
    if len(s) <= len(p):
        if s == p:
            indices.append(0)
        return indices
    for i in range(len(s)-len(p)+1):
        j = i + 1
        tmp = s[i]
        counter = 0
        while(counter < window_size):
            tmp = tmp + s[j]
            j = j + 1
            counter = counter + 1
        if tmp in set_of_anagrams:
            indices.append(i)
    return indices
        
#print(return_indices("abcdaebcai","abc"))
print(return_indices("baa","aa"))
