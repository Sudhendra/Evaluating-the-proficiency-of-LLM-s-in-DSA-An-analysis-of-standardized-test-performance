import pytest
from q_2555_maximizeWinFromTwoSegments import Solution


@pytest.mark.parametrize(
    "prizePositions, k, output", [([1, 1, 2, 2, 3, 3, 5], 2, 7), ([1, 2, 3, 4], 0, 2)]
)
class TestSolution:
    def test_maximizeWin(self, prizePositions: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.maximizeWin(
                prizePositions,
                k,
            )
            == output
        )
