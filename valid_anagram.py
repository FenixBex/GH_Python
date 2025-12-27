'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

'''
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        lst_lat_alph = [0] * 26
        const_val = ord('a')
        for char1, char2 in zip(s, t):
            lst_lat_alph[ord(char1) - const_val] += 1
            lst_lat_alph[ord(char2) - const_val] -= 1
        return all(x == 0 for x in lst_lat_alph)
