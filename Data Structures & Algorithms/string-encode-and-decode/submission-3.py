class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            delimeter = str(len(s)) + "#"
            # froms strs: "abc", "de" --> res = "3#abc2#de" 
            res = res + delimeter + s 

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        while len(s) > 0:
            index_pound = s.find("#")
            ss_len = int(s[0:index_pound])
            curr_ss = ""
            end_index = index_pound + 1 + ss_len
            res.append(s[index_pound + 1: end_index])
            s = s[end_index:]

        return res

