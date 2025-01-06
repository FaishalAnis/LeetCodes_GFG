/*Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.
Note: Consider the array as circular.
Examples :
Input: arr[] = [1, 2, 3, 4, 5], d = 2
Output: [3, 4, 5, 1, 2]
Explanation: when rotated by 2 elements, it becomes 3 4 5 1 2.*/

class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d %= n
        arr[0:d] = reversed(arr[0:d])
        arr[d:n] = reversed(arr[d:n])
        arr[0:n] = reversed(arr[0:n])

/*
ROTATE AN ARRAY FOR LEETCODE
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Handle cases where k is larger than the length of the array
        n = len(nums)
        k = k % n  # In case k is larger than n

        # Step 1: Reverse the entire array
        self.reverse(nums, 0, n - 1)
        
        # Step 2: Reverse the first k elements
        self.reverse(nums, 0, k - 1)
        
        # Step 3: Reverse the remaining elements
        self.reverse(nums, k, n - 1)

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        """
        Reverse the elements in nums from index `start` to index `end`.
        """
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
*/
