class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        l1, l2 = 0, 0
        if len(nums1) > len(nums2):
            nums2 = nums2 + [float('inf')] * (len(nums1) - len(nums2))
            nums1 = nums1 + [float('inf')]
        else:
            nums1 = nums1 + [float('inf')] * (len(nums2) - len(nums1)+1)
            nums2 = nums2 + [float('inf')]
        a = []
        while (l1<len(nums1) and l2<len(nums2)):
            if nums1[l1]>nums2[l2]:
                a.append(nums2[l2])
                l2+=1
            elif nums1[l1]==nums2[l2]:
                a.append(nums1[l1])
                a.append(nums2[l2])
                l1+=1
                l2+=1
            else:
                a.append(nums1[l1])
                l1+=1
        a = a[:-2]
        n1 = len(a)
        print(a)
        if n1%2!=0:
            return a[n1//2]
        else:
            return (a[n1//2]+a[n1//2-1])/2