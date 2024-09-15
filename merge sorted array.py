from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1

        # merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        # fill nums1 with leftover nums2 elements
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1


if __name__ == '__main__':
    arr1 = [1, 2, 3, 0, 0, 0]
    arr2 = [2, 5, 6]
    # number of  real elements in each array
    m = 3
    n = 3
    Solution().merge(arr1, m, arr2, n)
    print(arr1)