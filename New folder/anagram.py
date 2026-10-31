"""
Problem:
Given two strings s1 and s2, check if one is an anagram of the other.


input:
s1 = abaabc
s2 = cabaab

# Implement a Hash Set using array where hash(char) = i; e.g hash("a") = 0
s1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
s2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]



strings = [s1, s2]
for i in range(len(sets)):
    set = sets[i]
    string = strings[i]

    for character in string:
        if character not in set:
            set.add(character)




"""


def isAnagram(s1, s2):
    if len(s1) != len(s2): #if 
        return False

    # Implemented Set using Array; hash(char) = idx 
    set1 = [0]*26
    set2 = [0]*26


    strings = [s1, s2]
    sets = [set1, set2]
    for i in range(2):
        curr_set = sets[i]
        curr_string = strings[i]

        for character in curr_string:
            hash_str = ord(character) - ord("a")
            curr_set[hash_str] += 1

    for i in range(26):
        if set1[i] != set2[i]:
            return False
    return True



def main():
    s1 = input()
    s2 = input()



    # print("0, "*26)

    isAnagramString = isAnagram(s1, s2)
    print(isAnagramString)





main()