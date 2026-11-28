class TimeMap:

    def __init__(self):
        
        self.hmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.hmap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:

        arr = self.hmap[key]
        if len(arr) == 0: return ""

        def bsearch(l,r): 

            if l > r: return ""

            if l == r: 
                if arr[l][0] <= timestamp: return arr[l][1]
                else: return ""
            
            if l == r-1: 
                if arr[r][0] <= timestamp: return arr[r][1]
                if arr[l][0] <= timestamp: return arr[l][1]
                return ""


            m = (l+r)//2

            if arr[m][0] < timestamp: 
                return bsearch(m,r)
            if arr[m][0] > timestamp: 
                return bsearch(l,m-1)
            if arr[m][0] == timestamp: return arr[m][1]



        return bsearch(0,len(arr)-1)

        
