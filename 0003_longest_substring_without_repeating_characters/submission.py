class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        ret = []
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if s[j] in s[i:j]:
                    ret.append(j-i)
                    break
                else:
                    ret.append(j-i+1)
        return max(ret)
