class Solution:
    def convert(self,s:str,numRows:int) -> str:
        if numRows < 2:  #numRows不能换成s，s字符串后面不能直接＜，会报错
            return s
        res = ["" for _ in range (numRows)]
        flag = -1   #
        i = 0
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return "".join(res)#res的连接不需要任何分隔符隔开
a = Solution()
print(a.convert("PAYPALISHIRING",4))       