class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        r = 0
        l=0
        for i in range(len(arr)):
            if arr[i] > x: 
                r = i
                l = i-1
                break

            if i == len(arr)-1:
                l = len(arr)-1
                r = len(arr)
        
        res = []
        for i in range(k):
            print(l,r)
            if l>-1 and r<len(arr) :
                if arr[r] - x < x - arr[l]:
                    res.append(arr[r])
                    r+=1
                else:
                    res.append(arr[l])
                    l-=1

            elif l>-1: 
                res.append(arr[l])
                l-=1
            
            elif r<len(arr):
                res.append(arr[r])
                r+=1

        
        res.sort()
        return res
