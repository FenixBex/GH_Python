class Solution(object):
    def isValid(self, s):
        if len(s) < 2:
            return False
        new_lst = []
        for ch in s:
            if ch in "({[":
                new_lst.append(ch)
            elif ch in ")}]" and new_lst == []:
                return False
            else:
                if (new_lst[-1] == '(' and ch != ')') or (new_lst[-1] == '{' and ch != '}') or (new_lst[-1] == '[' and ch != ']'):
                    return False
                new_lst.pop()
        return new_lst == []
