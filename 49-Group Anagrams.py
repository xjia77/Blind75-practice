class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        这道题就是对原有的str中每个子项进行字母排序，然后整体排序，相同的就加在的第一个相同的本体的后面。
        最后返回mp value。
        """

        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)
        
        return list(mp.values())
