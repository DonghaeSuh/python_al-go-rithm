# 정렬 후 짝수번째 합
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total=0
        for i in range(len(nums)):
            if i%2==0:
               total+=nums[i]
        return total

# 파이썬 다운 방식
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        return sum(sorted(nums)[::2])
