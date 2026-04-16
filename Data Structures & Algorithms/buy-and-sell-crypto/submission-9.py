class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we will utilize a two pointer technique casue we need to track two things
        # we'll have a left pointer and a right pointer, left for buys and right for sells. 
        # the logic:
        # 1. intialize the pointers and the maxprofit, 0,1 and 0 respectively. 
        # 2. we're going to check if the sell pointer is within our bounds and not at the end of the set. 
        # 3. if the buy price is less than the sell price then we'll compute the difference and add in the profit.
        # 4. after adding in our profit we will ensure that we check if the profit we got is more than the previous one.
        # 5. if the profit is greater than the current max we have we'll update that to ensure that we are up to date. 
        # 5. if the buying price is more than the sell price indicating a negative differential then we will change the pointer to the sell pointer since that's a better opportunity. 
        # 6. after that we will iterate throughout with the r +=1 until we reach the end. 
        # 7. the goal is to do this with one iteration as opposed to multiple for effectivness and efficiency. 

        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
        