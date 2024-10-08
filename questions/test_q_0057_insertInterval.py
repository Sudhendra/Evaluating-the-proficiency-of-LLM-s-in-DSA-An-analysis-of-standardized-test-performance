import pytest
from q_0057_insertInterval import Solution


@pytest.mark.parametrize(
    "intervals, newInterval, output",
    [
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        (
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[1, 2], [3, 10], [12, 16]],
        ),
    ],
)
class TestSolution:
    def test_insert(
        self,
        intervals: List[List[int]],
        newInterval: List[int],
        output: List[List[int]],
    ):
        sc = Solution()
        assert (
            sc.insert(
                intervals,
                newInterval,
            )
            == output
        )
