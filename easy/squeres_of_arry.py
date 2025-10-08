class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = len(nums)-1, 0
        if l==0:
            return [nums[l]**2]
        a = []
        while r<l:
            kv_r, kv_l = nums[r]**2, nums[l]**2
            if kv_r>kv_l:
                a.append(kv_r)
                r+=1
            elif kv_r==kv_l:
                a.append(kv_l)
                l-=1
            else:
                a.append(kv_l)
                l-=1
        if kv_l>=kv_r:
            a.append(kv_r)
        else:
            a.append(kv_l)
        return a[::-1]