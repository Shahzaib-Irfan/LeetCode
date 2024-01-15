# This solution takes 58ms and beats 99.85% of users
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:

        x = nums1.copy()
        for i in nums2:
            x.append(i)

        x.sort()


        mid = (len(x) - 1) // 2

        if len(x) % 2 == 0:
            print()
            return (x[mid] + x[mid + 1]) / 2
        else:
            return x[mid]