from collections import defaultdict


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Compile dictionary in num:list[index] format
        nums_dict = defaultdict(list)
        for k, v in [(value, index) for index, value in enumerate(nums)]:
            nums_dict[k].append(v)

        for num in nums:
            complement = target - num
            if complement in nums_dict:
                if complement != num:
                    return nums_dict[num] + nums_dict[complement]
                elif len(nums_dict[num]) > 1:
                    return nums_dict[num]

        raise Exception("No sum found.")

if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]