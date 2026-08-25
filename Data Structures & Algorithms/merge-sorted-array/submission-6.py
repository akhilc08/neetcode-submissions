class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, i= len(nums1)-1-n, len(nums2)-1, len(nums1)-1

        while i>-1:
            print(i,p1,p2)
            print(nums1)
            
            if p2 <0: 
                nums1[i] = nums1[p1]
                p1-=1
            elif p1 <0:

                nums1[i] = nums2[p2]

                p2-=1
            elif nums2[p2]>nums1[p1]:
                nums1[i] = nums2[p2]
                p2-=1
            elif nums2[p2]<nums1[p1]:
                nums1[i] = nums1[p1]
                p1-=1
            elif nums2[p2]==nums1[p1]:
                nums1[i] = nums1[p1]
                p1-=1


            i-=1

