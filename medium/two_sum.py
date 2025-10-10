class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right, left = 0, len(numbers)-1
        while right<left:
            new_sum = numbers[left]+numbers[right]
            if new_sum==target:
                return [right+1, left+1]
            if new_sum>target:
                left-=1
            else:
                right+=1
        
        