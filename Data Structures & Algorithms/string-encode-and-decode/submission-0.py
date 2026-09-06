class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):  # Changed: len(str) -> len(s)
            j = i 
            while s[j] != "#":  # Changed: str[j] -> s[j]
                j += 1
            length = int(s[i:j])  # Changed: str[i:j] -> s[i:j]
            res.append(s[j + 1 : j + 1 + length])  # Changed: str -> s
            i = j + 1 + length
        return res
