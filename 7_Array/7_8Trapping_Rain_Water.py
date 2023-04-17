## 투 포인터
class Solution:
    def trap(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        left_max,right_max=height[left],height[right]
        count=0

        while left<right:
            left_max=max(left_max,height[left])
            right_max=max(right_max,height[right])

            if left_max<=right_max:
                count+=left_max-height[left]
                left+=1
            else:
                count+=right_max-height[right]
                right-=1
        return count
      
# 스택 쌓기
class Solution:
    def trap(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        left_max,right_max=height[left],height[right]
        count=0

        while left<right:
            left_max=max(left_max,height[left])
            right_max=max(right_max,height[right])

            if left_max<=right_max:
                count+=left_max-height[left]
                left+=1
            else:
                count+=right_max-height[right]
                right-=1
        return count
