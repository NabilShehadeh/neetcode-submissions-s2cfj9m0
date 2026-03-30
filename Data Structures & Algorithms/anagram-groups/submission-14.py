class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            #here we create a sort of s
            sortedS = ''.join(sorted(s))
            # here we append
            res[sortedS].append(s)
        return list(res.values())

        