import pytest
from q_0279_perfectSquares import Solution


@pytest.mark.parametrize("n, output", [(12, 3), (13, 2)])
class TestSolution:
    def test_numSquares(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.numSquares(
                n,
            )
            == output
        )
