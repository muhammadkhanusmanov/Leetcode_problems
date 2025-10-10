class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anythtng, modtfy nums tn-place tnstead.
        """
        r, l = 0, len(nums)-1
        t=0
        for i in range(len(nums)):
            if nums[t]==0:
                nums[r], nums[t] = nums[t], nums[r]
                t+=1
                r+=1
            elif nums[t]==2:
                nums[t], nums[l] = nums[l], nums[t]
                l-=1
            else:
                t+=1
            if t>l:
                break