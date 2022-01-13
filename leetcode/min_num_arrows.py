
# XY Plane
# points: List[List[int]]
# one point is [xstart, xend]
# y coord is not known
# arrows shoot up from a x position and hit all y positions at that x
# balloon is burst if xstart <= xshoot <= xend
# no limit to arrows
# return minimum number of arrows needed to burst all balloons given points

from typing import List, Set

def min_num_arrows(points: List[List[int]]) -> int:
    
    num_arrows: int = len(points)

    # shooting at the interlapping points
    #    --   
    #   ----
    # ----
    #       --
    #           -

    # Sort by the x starting point
    points = sorted(points, map=lambda x: x[0])

    # Arrows shot?
    # arrows: Set[int] = {}

    popped: List[bool] = [False] * len(points)

    for i in range(len(points)):
        for j in range(i, len(points)):
            # Check only overlapping balloons
            if points[j][0] > points[i][1]:
                # if not popped[i]:
                    # popped[i] = True
                    # arrows.add(points[i][1])
                break
            else:
                num_arrows -= 1
                # popped[j] = True

                # arrows.add(points[i][1])

            
    return num_arrows


def min_num_arrows(points: List[List[int]]) -> int:
    # Space O(1) ~ O(1)
    # Time O(NlogN + N*overlap) ~ O(NlogN)
    num_arrows: int = len(points)
    # Sort by the x starting point
    points = sorted(points, key=lambda x: x[0])
    # Check for overlapping balloons
    popped: List[bool] = [False] * len(points)
    for i in range(len(points)):
        if popped[i]:
            continue
        for j in range(i, len(points)):
            if points[j][0] > points[i][1]:
                popped[i] = True
                break
            else:
                num_arrows -= 1
    return num_arrows

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Space O(1) ~ O(1)
        # Time O(NlogN + N*overlap) ~ O(NlogN)
        num_arrows: int = len(points)
        # Sort by the x starting point
        points = sorted(points, key=lambda x: x[0])
        # Check for overlapping balloons
        interval: List[int] = points[0]
        for i in range(1, len(points)):
            if points[i][0] <= interval[1]:
                num_arrows -= 1
                interval = [max(points[i][0], interval[0]), \
                            min(points[i][1], interval[1])]
            else:
                interval = points[i]
        return num_arrows
