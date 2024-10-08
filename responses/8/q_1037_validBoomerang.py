from typing import List

class Solution:
    """Given an array `points` where `points[i] = [xi, yi]` represents a point on the **X-Y** plane, return `true` *if these points are a **boomerang***.

    A **boomerang** is a set of three points that are **all distinct** and **not in a straight line**.
    """

    def isBoomerang(self, points: List[List[int]) -> bool:
        if (points[0][0] == points[1][0] and points[0][1] == points[1][1]) or \
           (points[0][0] == points[2][0] and points[0][1] == points[2][1]) or \
           (points[1][0] == points[2][0] and points[1][1] == points[2][1]):
            return False

        return (points[0][0] * (points[1][1] - points[2][1]) +
                points[1][0] * (points[2][1] - points[0][1]) +
                points[2][0] * (points[0][1] - points[1][1])) != 0
