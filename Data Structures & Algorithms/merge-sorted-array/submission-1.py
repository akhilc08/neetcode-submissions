class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1,p2 = 0,0
        while p1<len(nums1) and p2<len(nums2):
            print(nums1)
            if nums2[p2] < nums1[p1] or (p1-p2) == m: 
                temp = nums1[p1]
                nums1[p1] = nums2[p2]

                for tp in range(p1+1,len(nums1)):
                    temp2 = nums1[tp]
                    nums1[tp] = temp
                    temp = temp2
                    tp+=1

                p2+=1
            else: 
                p1+=1

        

