class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        这道题是找股票最大利润，将这个利润初始为0，对每日股票价格集合进行遍历，
        先设第一个股票价格为最小，之后如有更大的，进行替换，然后每轮返回res和当前价格与最低价格差的最大值，
        当遍历结束时，返回res值。
        """

        res = 0   
        lowest = prices[0]
        for i in prices:
            if i < lowest:
                lowest = i
            res = max(res, i - lowest)
        return res
