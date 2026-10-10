class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for index, num in enumerate(nums):

            temp_num = target - num

            if temp_num in seen:
                return [seen[temp_num], index]

            seen[num] = index

        return []