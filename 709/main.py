class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()


if __name__ == "__main__":
    s = Solution()
    assert s.toLowerCase("Hello") == "hello"
    assert s.toLowerCase("here") == "here"
    assert s.toLowerCase("LOVELY") == "lovely"