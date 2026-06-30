class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_i = 1
        for curr in range (1,len(nums)):
            if nums[curr] != nums[curr-1]:
                nums[write_i]=nums[curr]
                write_i +=1
        return write_i
