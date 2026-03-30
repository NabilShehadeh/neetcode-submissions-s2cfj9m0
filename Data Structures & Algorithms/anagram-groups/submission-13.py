class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            # here we need to join the sorted S
            sortedS = ''.join(sorted(s))
            # here we append the sorteds with s
            res[sortedS].append(s)
            # we return our result
        return list(res.values())
        