class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                result.append(i)
            else:
                if len(result) == 0:
                    return False
                elif i == ")" and result[-1] == "(":
                    result = result[:-1]
                elif i == "}" and result[-1] == "{":
                    result = result[:-1]
                elif i == "]" and result[-1] == "[":
                    result = result[:-1]
                else:
                    return False
        if len(result) == 0:
            return True
        else:
            return False