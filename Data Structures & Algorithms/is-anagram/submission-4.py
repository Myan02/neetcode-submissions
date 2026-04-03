class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return second_attempt(s, t)

        

def first_attempt(s: str, t: str) -> bool:

    #slowly reduce string t until it is empty
    # too slow
    if len(s) != len(t):
        return False
    else:
        for letter in s:
            if letter in t:
                t = t.replace(letter, '', 1)
                print(t)
            else:
                return False
    
    return True

def second_attempt(s: str, t: str) -> bool:
    
    # keep track of the number of occurences of each letter
    # key = letter
    # value = number of occurences

    s_table = {}
    t_table = {}

    for elem in s:
        if elem not in s_table.keys():
            s_table[elem] = 0
        else:
            s_table[elem] += 1
    
    for elem in t:
        if elem not in t_table.keys():
            t_table[elem] = 0
        else:
            t_table[elem] += 1
    
    if s_table == t_table:
        return True
    
    return False
