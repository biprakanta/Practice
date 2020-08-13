# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution(object):
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        ref_set = set()
        ptr1=0
        ptr2=1
        max_len=1
        ref_set.add(s[ptr1])
        while ptr2 < len(s):
            if s[ptr2] in ref_set:
                max_len = max((ptr2-ptr1),max_len)
                ref_set.clear()
                ptr1+=1
                ref_set.add(s[ptr1])
                ptr2=ptr1+1
            else:
                ref_set.add(s[ptr2])
                ptr2+=1
        if ref_set:
            max_len = max((ptr2-ptr1),max_len)
        return max_len
