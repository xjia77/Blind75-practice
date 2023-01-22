class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        这道题的思路是，建立一个哈希表，把每个数据和对应的索引存在表中，for循环，
        一旦找到target-当前数据的值存放在哈希表中，就return对应的索引。
        """

        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
