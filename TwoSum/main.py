class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = list()
        for i in range(len(nums)):
            mytarget = target - nums[i]
            if mytarget in nums and i != nums.index(mytarget):
                l.append(i)
                l.append(nums.index(mytarget))
                break
        return l


s = Solution()
print(s.twoSum([3,2,4],6))
print(s.twoSum([0,4,3,0],0))
print(s.twoSum([-3,4,3,90],0))
