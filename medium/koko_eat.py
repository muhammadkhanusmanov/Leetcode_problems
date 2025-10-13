def check(piles, k):
    cur_h = 0
    for pile in piles:
        cur_h=cur_h + (pile//k) + (1 if pile%k>0 else 0)
    return cur_h

class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        if len(piles) == 1:
            return (piles[0]//h) + (1 if piles[0]%h>0 else 0)
        min_k = min(piles)
        if check(piles, min_k) <= h:
            min_k = 0
        max_k = max(piles)
        while min_k <= max_k:
            mid_k = (min_k + max_k) // 2 + (1 if (min_k + max_k) % 2 == 1 else 0)
            cur_h = check(piles, mid_k)
            if cur_h > h:
                min_k = mid_k
            else:
                if check(piles, mid_k-1) > h:
                    return mid_k
                max_k = mid_k