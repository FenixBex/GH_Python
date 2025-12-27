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
