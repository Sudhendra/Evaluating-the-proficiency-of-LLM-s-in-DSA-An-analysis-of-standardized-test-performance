import pytest
from q_2662_minimumCostOfAPathWithSpecialRoads import Solution


@pytest.mark.parametrize(
    "start, target, specialRoads, output",
    [
        ([1, 1], [4, 5], [[1, 2, 3, 3, 2], [3, 4, 4, 5, 1]], 5),
        ([3, 2], [5, 7], [[3, 2, 3, 4, 4], [3, 3, 5, 5, 5], [3, 4, 5, 6, 6]], 7),
    ],
)
class TestSolution:
    def test_minimumCost(
        self,
        start: List[int],
        target: List[int],
        specialRoads: List[List[int]],
        output: int,
    ):
        sc = Solution()
        assert (
            sc.minimumCost(
                start,
                target,
                specialRoads,
            )
            == output
        )
