import pytest
from q_2463_minimumTotalDistanceTraveled import Solution


@pytest.mark.parametrize(
    "robot, factory, output",
    [([0, 4, 6], [[2, 2], [6, 2]], 4), ([1, -1], [[-2, 1], [2, 1]], 2)],
)
class TestSolution:
    def test_minimumTotalDistance(
        self, robot: List[int], factory: List[List[int]], output: int
    ):
        sc = Solution()
        assert (
            sc.minimumTotalDistance(
                robot,
                factory,
            )
            == output
        )
