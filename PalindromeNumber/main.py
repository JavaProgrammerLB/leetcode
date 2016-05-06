class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            s = str(x)
        else :
            return False
        l = list(s)
        for i in range(int(len(l) / 2)):
            if l[i] != l[len(l) - 1 - i] :
                return False
        else:
            return True
