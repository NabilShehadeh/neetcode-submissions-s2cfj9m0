class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # first thing we could try to do is compute every single subarray
        # for the i which is the starting value till n-1 then we want to get the ending index
        # for j = i .... n - 1 till we get through the entire array
        # i is the start and j is the end
        # third loop for the k = ranges from i till j (reps the subarray)
        # since we have three loops our time complexity would be around 3-4 loops

        # we can save time by computing, do we need the negative numbers, so we can essentially disregard the negative numbers. 
        # only regard the positive numbers. 
        # here we can add 3 + 2 + 1  = 6 - 5 = 1 + 4 = 5 the max subarray is 5
        # kind of a sliding window
        # linear time alg O(n), removing any negative prefix as we compute the total sum

        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0: 
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub
        