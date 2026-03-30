class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we intialize this problem with a default dictionary, 
        res = defaultdict(list)
        for s in strs:
            # here we'll create a sorted situation where we'll set up the comparisons
            sortedS = ''.join(sorted(s))
            # then we'll compare
            res[sortedS].append(s)
        return list(res.values())
        