import pytest
from q_2106_maximumFruitsHarvestedAfterAtMostKSteps import Solution


@pytest.mark.parametrize(
    "fruits, startPos, k, output",
    [
        ([[2, 8], [6, 3], [8, 6]], 5, 4, 9),
        ([[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]], 5, 4, 14),
        ([[0, 3], [6, 4], [8, 5]], 3, 2, 0),
    ],
)
class TestSolution:
    def test_maxTotalFruits(
        self, fruits: List[List[int]], startPos: int, k: int, output: int
    ):
        sc = Solution()
        assert (
            sc.maxTotalFruits(
                fruits,
                startPos,
                k,
            )
            == output
        )
