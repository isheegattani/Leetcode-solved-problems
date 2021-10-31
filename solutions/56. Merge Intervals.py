class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key=lambda x: x[0])
        
        o=[]
        for i in intervals:
            if not o or o[-1][1]<i[0]:
                o.append(i)
            else:
                o[-1][1]=max(o[-1][1],i[1])
        return o
        
