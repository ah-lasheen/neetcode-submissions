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
        last_pound = s.rfind("#")
        while len(s) > 0:
            index_pound = s.find("#")
            ss_len = int(s[0:index_pound])
            curr_ss = ""

            if last_pound == index_pound:
                curr_ss = s[index_pound + 1:]
                res.append(curr_ss)
                s = ""
            else:
                curr_ss = s[index_pound + 1: index_pound + 1 + ss_len]
                res.append(curr_ss)
                s = s[index_pound + 1 + ss_len:]

        return res

