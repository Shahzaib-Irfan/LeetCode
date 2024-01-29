def removeDuplicates(self, nums: List[int]) -> int:
        mapping = {}
        for i in nums:
            mapping[i] = 0

        i = 0
        while i < len(nums):
            if mapping[nums[i]] != 0:
                nums.pop(i)
            else:
                mapping[nums[i]] += 1
                i += 1
