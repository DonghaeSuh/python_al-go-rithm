# 브루트 포스
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for k in range(i+1,len(nums)):
                if nums[i]+nums[k]==target:
                    return [i,k]
                    
# in 을 이용한 탐색
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for k in range(i+1,len(nums)):
                if nums[i]+nums[k]==target:
                    return [i,k]
                  
                  
# 첫 번째 수를 뺀 결과 키 조회
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict={}
        for i,num in enumerate(nums):
            num_dict[num]=i
        
        for i,num in enumerate(nums):
            answer=target-num
            if answer in num_dict and num_dict[answer]!=i:
                return [i,num_dict[answer]]
              
# 조회 구조 개선
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict={}
        for i,num in enumerate(nums):
            if target-num in num_dict:
                return [i,num_dict[target-num]]
            num_dict[num]=i
