class Solution:
    def maxArea(self, heights: List[int]) -> int:
        x = 0
        y = len(heights) -1

        max = (y-x)*min(heights[x],heights[y])
        while x<y:
            if heights[x] < heights[y]:
                x+=1
                newcontainer = (y-x)*min(heights[x],heights[y])
                if newcontainer>max:
                    max = newcontainer
            else:
                y-=1
                newcontainer = (y-x)*min(heights[x],heights[y])
                if newcontainer>max:
                    max = newcontainer
        return max





        