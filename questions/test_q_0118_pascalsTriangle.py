import pytest
from q_0118_pascalsTriangle import Solution


@pytest.mark.parametrize(
    "numRows, output",
    [(5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]), (1, [[1]])],
)
class TestSolution:
    def test_generate(self, numRows: int, output: List[List[int]]):
        sc = Solution()
        assert (
            sc.generate(
                numRows,
            )
            == output
        )
