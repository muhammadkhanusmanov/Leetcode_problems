class Solution:
    def maxArea(self, height: List[int]) -> int:
        right, left = 0, len(height)-1
        big=0
        while right<left:
            new_big = min(height[right],height[left]) * (left-right)
            if big<new_big:
                big=new_big
            if height[right]>height[left]:
                left-=1
                    
            else:
                right+=1
        
        return big    