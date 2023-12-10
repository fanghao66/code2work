

#最开始我的解法
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        max_length = len(set(s))
        max_l=0
        while max_length !=0:
            end_index = len(s)-max_length+1
            for index in range(end_index):
                k=s[index:index+max_length]
                if len(set(k)) == len(k):
                    return len(k)
            max_length -=1
        return max_length

#优化解法
#不重复字串的最大长度，利用字典保存每个字符的位置，如果出现相同字符则更新字符位置为新字符出现的位置，并同时更新开始指示为旧字符的位置
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = -1
        max=0
        d={}
        for i in range(len(s)):
            if s[i] in d and d[s[i]] >start:
                start = d[s[i]]
                d[s[i]]=i
            else:
                d[s[i]]=i
                if i -start >max:
                    max=i-start
        return max

