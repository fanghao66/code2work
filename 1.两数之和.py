'''给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。'''
#基础解法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for (num,value) in enumerate(nums):
            start_index = num+1
            if target - value in nums[num+1:]:
                return [num,nums[num+1:].index(target - value)+start_index]

#利用hash表加速运算
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        past_dict={}
        for (num,value) in enumerate(nums):
            if target-value in past_dict.keys():
                return (num,past_dict[target-value])
            past_dict[value]=num