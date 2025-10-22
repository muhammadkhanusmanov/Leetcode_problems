def maxAdjacentDistance(nums) -> int:
        max_n = nums[0]
        min_n = nums[0]
        for n in nums:
            if n>=max_n:
                max_n = n
            if min_n>=n:
                min_n=n
            print(max_n,min_n)
        return max_n - min_n
print(maxAdjacentDistance([3,2,-5,-3]))  # Output: 4