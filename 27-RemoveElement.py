def removeElement(self, nums: List[int], val: int) -> int:
        isNotCleaned = True
        i = 0
        while isNotCleaned:
            if i == len(nums):
                break
            if nums[i] == val:
                nums.remove(nums[i])
            else:
                i += 1