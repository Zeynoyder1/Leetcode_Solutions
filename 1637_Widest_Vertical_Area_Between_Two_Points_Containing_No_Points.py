class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        points.sort()
        diff = 0
        max = 0
        for i in range(1,len(points)):
             diff = points[i][0] - points[i-1][0]
             if diff > max:
                max = diff
        return max
