class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        这道题是返回str中的k个最频繁的元素，思路是先调用collections.Counter进行无序化集合，然后
        使用most_common返回最长遇到的k个元素。
        """

        count = collections.Counter(nums)
        return [i[0] for i in count.most_common(k)]
