class Solution:

    def bsearch(self, lst, target, l, r):
        if r<l: 
            return False

        m = (r-l)//2+l
        print(l,r,m)

        if lst[m] == target: return True
        elif lst[m] > target: return self.bsearch(lst, target, l, m-1)
        else: return self.bsearch(lst,target, m+1, r)

    def search(self, matrix, target, t, b):

        if b<t: 
            return False
        if b==t: 
            print(matrix[b]) 
            return self.bsearch(matrix[b], target, 0, len(matrix[b])-1)
        

        m = (b-t)//2+t
        if matrix[m][0] == target: return True
        elif matrix[m][0] > target: return self.search(matrix, target, t, m-1)
        else: 
            if target < matrix[m+1][0]: 
                return self.bsearch(matrix[m], target, 0, len(matrix[m])-1)
            else: 
                return self.search(matrix, target, m+1, b)


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.search(matrix, target, 0, len(matrix)-1)