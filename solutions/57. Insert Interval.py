class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        newstart=newInterval[0]
        newend=newInterval[1]
        i=0
        o=[]
        N=len(intervals)
        while i<N and intervals[i][0]<newstart:
            o.append(intervals[i])
            i+=1
        if not o or o[-1][1]<newstart:
            o.append(newInterval)
        else:
            o[-1][1]=max(o[-1][1],newend)
        while i<N:
            newstart,newend=intervals[i]
            if o[-1][1]<newstart:
                o.append(intervals[i])
            else:
                o[-1][1]=max(o[-1][1],newend)
            i+=1
        return o
​
    
    
