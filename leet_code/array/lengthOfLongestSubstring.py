"""
 Address: https://leetcode.com/problems/longest-substring-without-repeating-characters/
 Thinking: 最长无重复子串。数据结构中有KMP匹配字符串算法，和这个有一些不一样.
           分两步，第一步找到无重复字串，第二步，找到最长的
           btw. 总结：查找用dict hashtable。
 Test: set 没有index 方法。 ***循环时不能改变循环体结构，即不能增删***
 Review:
    字符串匹配:
        朴素字符串匹配
        KMP字符串匹配算法
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_s = []
        sub_len = 0
        for c in s:
            if c in sub_s:
                if len(sub_s) > sub_len:
                    sub_len = len(sub_s)
                sub_s = sub_s[sub_s.index(c) + 1:]
            sub_s.append(c)
        return max(len(sub_s), sub_len)


"""
Reference:
    solution2: 时间复杂度在找到是否重复元素上，别人例子，记录substring下标，然后substring用set. 不删除元素，只用上下标,不好理解(实际测试，并没有提高很多)。
               自己改进方向用hashtable(提升很大)
"""


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_s = dict()
        sub_len = 0
        cur = 0
        for i, c in enumerate(s):
            if c in sub_s and cur <= sub_s[c]:
                sub_len = max(sub_len, i - cur)
                cur = sub_s[c] + 1
            sub_s[c] = i
        return max(len(s) - cur, sub_len)
