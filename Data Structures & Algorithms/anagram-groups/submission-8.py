class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # first we'll create a default dictionary
        # then iterate through the sorted strings
        # then append the strings
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
        