def hisoblagich(height,v):
    b=[]
    m=height[0]
    s=0
    for i in range(1,len(height)):
            if m<=height[i]:
                if b:
                    d = min(m, height[i])
                    for k in b:
                        s+=d-k
                    v+=s
                    s=0
                    b=[]
                m=height[i]
            else:
                b.append(height[i])
    return [v, b, m]

class Solution:
    def trap(self, height) -> int:
        a = hisoblagich(height, 0)
        v, b = a[0], a[1]
        if a:
            b = [a[-1]]+b
            a = hisoblagich(b[::-1], v)
        return a[0]