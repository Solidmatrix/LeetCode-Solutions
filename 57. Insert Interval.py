# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        intervals = sorted(intervals, key = lambda x: x.start)
        for i in xrange(len(intervals)-1, 0, -1):
            while i < len(intervals) and intervals[i].start <= intervals[i-1].end:
                intervals[i-1].end = max(intervals[i-1].end, intervals[i].end)
                del intervals[i]
        return intervals