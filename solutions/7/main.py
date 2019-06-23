class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        rtype = "{}{}".format(
            "-",
            x.strip("-")[::-1]) if x.startswith("-") else x[::-1]
        rtype = int(rtype)
        return rtype if (-2**31 - 1) < rtype < (2**31 - 1) else 0

if __name__ == "__main__":
    s = Solution()
    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
    assert s.reverse(120) == 21