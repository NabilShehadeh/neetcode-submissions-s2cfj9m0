class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # default dictionary
        result = defaultdict(list)
        for s in strs: 
            count = [0] * 26
            for c in s:# utilize ascii
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s)
        return list(result.values())