class Solution(object):
    def isAnagram(self, s, t):
        """
        这道题目的思路就是二者各自建立一个hashmap,存储字符和这个字符出现的次数。如果一一对应，则说明true。
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        "这里是判断长度，如果长度都不相等，则肯定是false"

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) "新出现一个，存在次数就加一"
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT