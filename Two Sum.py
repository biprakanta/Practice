# https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        arr=[]
        for idx in range(len(nums)):
            arr.append([nums[idx], idx])
        arr.sort()
        i=0
        j=len(arr)-1
        while i<j:
            if arr[i][0]+arr[j][0]==target:
                return [arr[i][1],arr[j][1]]
            elif arr[i][0]+arr[j][0]>target:
                j-=1
            else:
                i+=1
