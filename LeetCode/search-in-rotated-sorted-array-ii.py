# problem leetcode link : https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

class Solution:
    def findMinIndex(self,arr):
        start = 0
        end = len(arr) - 1
        n = len(arr)
        while start <= end:
            if arr[start] <= arr[end]:
                return start
            mid = int(start + ((end - start)/2))
            prev = (mid + n - 1 ) % n
            next = (mid + 1) % n
            if arr[mid] < arr[prev] and arr[mid] < arr[next]:
                return mid
            elif arr[start] <= arr[mid]:
                start = mid + 1
            elif arr[mid] <= arr[end]:
                end = mid - 1
    
    def binarySearch(self,arr,start,end,target):
        while start <= end:
            mid = int(start + ((end - start)/2))
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                start = mid + 1
            elif arr[mid] > target:
                end = mid - 1
        return False
    
    def search(self, nums: List[int], target: int) -> bool:
        minIndex = self.findMinIndex(nums)
        leftArr = self.binarySearch(nums,0,minIndex - 1, target)
        rightArr = self.binarySearch(nums,minIndex,len(nums) -1 , target)
        if leftArr != False:
            return leftArr
        elif rightArr != False:
            return rightArr
        return False
    
s = Solution()
s.search()
        