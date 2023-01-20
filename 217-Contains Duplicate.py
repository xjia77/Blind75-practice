class Solution(object):
    def containsDuplicate(self, nums):
        """
        这道题的思路就是使用hashset,一次将数组中的元素存入，并在每一回合检查当前要插入的元素在hashset中是否存在，如果存在则说明存在至少有两个，则return true.
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)   
        return False
