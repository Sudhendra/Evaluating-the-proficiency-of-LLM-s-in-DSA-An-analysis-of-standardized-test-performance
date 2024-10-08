import pytest
from q_1253_reconstructA2RowBinaryMatrix import Solution


@pytest.mark.parametrize(
    "upper, lower, colsum, output",
    [
        (2, 1, [1, 1, 1], [[1, 1, 0], [0, 0, 1]]),
        (2, 3, [2, 2, 1, 1], []),
        (
            5,
            5,
            [2, 1, 2, 0, 1, 0, 1, 2, 0, 1],
            [[1, 1, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0, 1, 1, 0, 1]],
        ),
    ],
)
class TestSolution:
    def test_reconstructMatrix(
        self, upper: int, lower: int, colsum: List[int], output: List[List[int]]
    ):
        sc = Solution()
        assert (
            sc.reconstructMatrix(
                upper,
                lower,
                colsum,
            )
            == output
        )
