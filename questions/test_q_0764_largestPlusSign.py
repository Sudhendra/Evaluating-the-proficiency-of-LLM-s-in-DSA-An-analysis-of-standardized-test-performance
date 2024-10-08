import pytest
from q_0764_largestPlusSign import Solution


@pytest.mark.parametrize("n, mines, output", [(5, [[4, 2]], 2), (1, [[0, 0]], 0)])
class TestSolution:
    def test_orderOfLargestPlusSign(self, n: int, mines: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.orderOfLargestPlusSign(
                n,
                mines,
            )
            == output
        )
