class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        x1 = abs(x)
        while (x1 != 0):
            tmp = x1 % 10  #通过取余数得到最后一位数字，往复循环得到最后一位数字
            if res > 214748364 or (res == 214748364 and tmp > 7):  #如果res>7，一定是比倒数第二位6大
                return 0
            res = res*10 + tmp  #将之前取得最后一位数（余数），反转到第一位数
            x1 //= 10  #python3支持//取整；java支持/取整
        if x > 0:
            return res
        else:
            return -res  #程序起始abs了，程序结束要将‘-’添上
    
a = Solution()
print(a.reverse(77708))  #注意！不要输入"77708"，会error字符串类型不对
    