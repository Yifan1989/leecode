class Solution:
    def longestPalindrome(self,s:str) -> str:
        n = len(s)
        if n < 2:
            return s
        #初始化变量max_len;begin;dp二维数组
        max_len = 1
        begin = 0
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        #限定左右边界和子串长度
        for L in range(2,n+1):
            for i in range(n): #L=j-i+1 根据该式子可以推断出j的表达式  
                j = L + i -1
                if j >= n:
                    break

                if s[i] != s[j]:   #如果左右字符不相等，则该字符串一定不是回文
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True  #aba 字符串为长度3时，左右字符相等，则一定是回文
                    else:
                        dp[i][j] = dp[i+1][j-1]  #动态规划，当左右字符串相同时，该字符串是否是回文取决于内部子字符串是否是回文
                if dp[i][j] and j-i+1 > max_len:
                    max_len = j-i+1
                    begin = i
        return s[begin:begin+max_len]        
a = Solution()
print(a.longestPalindrome("dcdhkkha"))                  

        
#定义变量
#判断字符串 
#（1）长度为1，左右指针都指在一个字符上，一定是回文
#（2）长度大于2；限制左右指针和字符串的范围
#    i.左右指针字符不同，则不是回文
#    ii.左右指针字符相同，但是只有三个字符，一定是回文
#    iii.左右指针字符不同，则看子字符串是否是回文