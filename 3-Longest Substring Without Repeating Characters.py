class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        这道题是让返回一串字符串中最大不重复子串的长度。这里用到了滑动窗口的思想。
        即start，end。若是未重复的，start不动，end后移，若是重复的，start前移，最后，返回max函数的值。
        """

        charSet = set()
        start = 0
        res = 0

        for end in range(len(s)):
            while s[end] in charSet:
                charSet.remove(s[start])
                start += 1
            charSet.add(s[end])
            res = max(res, end - start + 1)
        return res
