import pytest
from q_2097_validArrangementOfPairs import Solution


@pytest.mark.parametrize(
    "pairs, output",
    [
        ([[5, 1], [4, 5], [11, 9], [9, 4]], [[11, 9], [9, 4], [4, 5], [5, 1]]),
        ([[1, 3], [3, 2], [2, 1]], [[1, 3], [3, 2], [2, 1]]),
        ([[1, 2], [1, 3], [2, 1]], [[1, 2], [2, 1], [1, 3]]),
    ],
)
class TestSolution:
    def test_validArrangement(self, pairs: List[List[int]], output: List[List[int]]):
        sc = Solution()
        assert (
            sc.validArrangement(
                pairs,
            )
            == output
        )
