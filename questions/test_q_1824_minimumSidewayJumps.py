import pytest
from q_1824_minimumSidewayJumps import Solution


@pytest.mark.parametrize(
    "obstacles, output",
    [([0, 1, 2, 3, 0], 2), ([0, 1, 1, 3, 3, 0], 0), ([0, 2, 1, 0, 3, 0], 2)],
)
class TestSolution:
    def test_minSideJumps(self, obstacles: List[int], output: int):
        sc = Solution()
        assert (
            sc.minSideJumps(
                obstacles,
            )
            == output
        )
