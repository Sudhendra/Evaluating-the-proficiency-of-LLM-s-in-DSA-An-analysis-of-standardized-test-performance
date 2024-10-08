import pytest
from q_0757_setIntersectionSizeAtLeastTwo import Solution


@pytest.mark.parametrize(
    "intervals, output",
    [
        ([[1, 3], [3, 7], [8, 9]], 5),
        ([[1, 3], [1, 4], [2, 5], [3, 5]], 3),
        ([[1, 2], [2, 3], [2, 4], [4, 5]], 5),
    ],
)
class TestSolution:
    def test_intersectionSizeTwo(self, intervals: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.intersectionSizeTwo(
                intervals,
            )
            == output
        )
