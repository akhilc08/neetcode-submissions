class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def find_row(u,d): 
            
            if u>d: return matrix[u]
            if u == d: 
                return matrix[u]

            if u == d-1: 
                if matrix[d][0] > target: 
                    return matrix[u]
                else: 
                    return matrix[d]
            
            m = (u+d)//2 

            if target < matrix[m][0]: 
                return find_row(u,m-1)
            if target >= matrix[m][0]:
                return find_row(m,d)
        
        row = find_row(0,len(matrix)-1)
        print(row)
        def bsearch(l,r,grid): 

            if l>r: return False
            if l == r: return grid[l] == target

            m = (l+r)//2

            if grid[m] > target: 
                return bsearch(l,m-1,grid)
            elif grid[m] < target: 
                return bsearch(m+1,r,grid)
            else: 
                return True

        return bsearch(0,len(row)-1,row)
        