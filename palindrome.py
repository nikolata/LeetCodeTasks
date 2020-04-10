class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x >= 0 and x < 9:
            return True
        normal_x = x
        reversed_x = []
        while x:
            reversed_x.append(x % 10)
            x = x // 10
        if reversed_x[0] == 0:
            return False
        summ = 0
        for num in reversed_x:
            summ = summ * 10 + num
        if normal_x == summ:
            return True
        else:
            return False

sol = Solution()
print(sol.isPalindrome(301))