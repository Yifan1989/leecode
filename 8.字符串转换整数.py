class Solution:
    def myAtoi(self,s:str) -> int:
        if not s:
            return 0
        res = 0
        n = len(s)
        flag = '+'
        for idx in range(n):      #找出所有空格符
            if s[idx] != ' ':
                break
        if s[idx] in '+-':        #找出第一个±号
            flag = s[idx]
            idx += 1
        for i in range(idx,n):
            if s[i] != '0':  
                idx = i
                break
        for i in range(idx,n):
            if s[i] not in '1234567890':
                break
            res = res*10 + int(s[i])
        if flag == '+':
            res = res
        else:
            res = - res
        if res < -2147483648:     #判断数值区间的上下届
            return -2147483648
        elif res > 2147483647:
            return 2147483647
        else:
            return res

a = Solution()
print(a.myAtoi("   -42"))