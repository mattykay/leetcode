class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        XOR = x ^ y
        return str(bin(XOR)[2:]).count('1') # bin() prefixed with 0b to indicate binary, so strip


if __name__ == "__main__":
    s = Solution()
    assert s.hammingDistance(1, 4) == 2