import pytest
from q_0851_loudAndRich import Solution


@pytest.mark.parametrize(
    "richer, quiet, output",
    [
        (
            [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]],
            [3, 2, 5, 4, 6, 1, 7, 0],
            [5, 5, 2, 5, 4, 5, 6, 7],
        ),
        ([], [0], [0]),
    ],
)
class TestSolution:
    def test_loudAndRich(
        self, richer: List[List[int]], quiet: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.loudAndRich(
                richer,
                quiet,
            )
            == output
        )
