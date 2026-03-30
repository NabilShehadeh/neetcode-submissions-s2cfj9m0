class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # default dictionary to map the strings/list
        # for each of the strings we'll create a sotrted version
        # then append all of them together 
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
        
        