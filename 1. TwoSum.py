def twoSum(nums: List[int], target: int) -> List[int]:

        mid = len(nums) // 2
        left = 0
        right = len(nums) - 1

        while left <= mid and right >= mid:

            if 0 == nums[left] + nums[left + 1] - target:
                return [left, left + 1]
            elif 0 == nums[right] + nums[right - 1] - target:
                return [right - 1, right]
            elif 0 == nums[left] + nums[right] - target:
                return [left, right]
            else:
                print(nums[left] + nums[right] - target)
                if right - 1 <= mid and left + 1 <= mid:
                    right = len(nums) - 1
                    if left + 1 > mid:
                        break
                    left += 1
                else:
                    right -= 1


        left = 0
        right = mid

        while left < mid - 1 and right > left:
            if nums[left] + nums[right] == target:
                return [left, right]
            else:
                if right - 1 > left:
                    right -= 1
                else:
                    right = mid
                    left += 1

        left = mid
        right = len(nums) - 1

        while left < len(nums) - 1 and right > left:
            if nums[left] + nums[right] == target:
                return [left, right]
            else:
                if right - 1 > left:
                    right -= 1
                else:
                    right = len(nums) - 1
                    left += 1

        return []