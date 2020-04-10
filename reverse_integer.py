class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        is_negative = False
        if x.count('-') == 1:
            is_negative = True
            x = x.replace('-', '')
        x = x[::-1]
        if len(x) != 1:
            while x[0] == '0':
                x = x[1::]
        if is_negative:
            return -int(x) if -int(x) >= -2**31 else 0
        else:
            return int(x) if int(x) <= 2**31 - 1 else 0


sol = Solution()
sol.reverse(123)
