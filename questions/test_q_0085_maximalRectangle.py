import pytest
from q_0085_maximalRectangle import Solution


@pytest.mark.parametrize(
    "matrix, output",
    [
        (
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ],
            6,
        ),
        ([["0"]], 0),
        ([["1"]], 1),
    ],
)
class TestSolution:
    def test_maximalRectangle(self, matrix: List[List[str]], output: int):
        sc = Solution()
        assert (
            sc.maximalRectangle(
                matrix,
            )
            == output
        )
