class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix, curr = "", ""
        i, j = 0, 1

        while i < len(strs[0]):
            curr = strs[0][i]
            
            while j < len(strs) and i < len(strs[j]) and curr == strs[j][i]:
                j += 1

            if j != len(strs): 
                break

            prefix += curr
            j = 1
            i += 1

        return prefix