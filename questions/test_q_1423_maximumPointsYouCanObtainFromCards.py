import pytest
from q_1423_maximumPointsYouCanObtainFromCards import Solution


@pytest.mark.parametrize(
    "cardPoints, k, output",
    [([1, 2, 3, 4, 5, 6, 1], 3, 12), ([2, 2, 2], 2, 4), ([9, 7, 7, 9, 7, 7, 9], 7, 55)],
)
class TestSolution:
    def test_maxScore(self, cardPoints: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.maxScore(
                cardPoints,
                k,
            )
            == output
        )
