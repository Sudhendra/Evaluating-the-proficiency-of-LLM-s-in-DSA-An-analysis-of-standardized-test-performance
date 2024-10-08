import pytest
from q_0502_ipo import Solution


@pytest.mark.parametrize(
    "k, w, profits, capital, output",
    [(2, 0, [1, 2, 3], [0, 1, 1], 4), (3, 0, [1, 2, 3], [0, 1, 2], 6)],
)
class TestSolution:
    def test_findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.findMaximizedCapital(
                k,
                w,
                profits,
                capital,
            )
            == output
        )
