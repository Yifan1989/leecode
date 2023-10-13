class Solution:
    def lengthOfLongestSustring(self,s:str) -> int:
        left = 0;right = 0   #左右指针初始都赋值为0
        res = 0              #最后返回的字符串长度输出值res
        if len(s) == 0:      #判断字符串长度为0
            return 0
        if s.count(s[0]) == len(s):#判断该字符串只有一个字符
            return 1
        if len(set(s)) == len(s):#无序且不重复集的长度=该字符串本身，则输出该字符串的长度
            return len(s)
        while right < len(s):  #当右指针比字符串长度小时，判断右指针所指字符是否已存在
            if s[right] not in s[left:right]:#不存在，则右指针+1，所+1在之前字段中未出现
                right += 1
                res = max(res,len(s[left:right]))
            else:
                while s[right] in s[left:right]:#若存在则左指针+1，将之前存在的相同字符剔除
                    left += 1
        return res
a = Solution()
print(a.lengthOfLongestSustring("abcdefghigdja"))         
        