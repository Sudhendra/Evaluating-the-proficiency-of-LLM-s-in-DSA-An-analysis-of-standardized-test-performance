import pytest
from q_0587_erectTheFence import Solution


@pytest.mark.parametrize(
    "trees, output",
    [
        (
            [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]],
            [[1, 1], [2, 0], [4, 2], [3, 3], [2, 4]],
        ),
        ([[1, 2], [2, 2], [4, 2]], [[4, 2], [2, 2], [1, 2]]),
    ],
)
class TestSolution:
    def test_outerTrees(self, trees: List[List[int]], output: List[List[int]]):
        sc = Solution()
        assert (
            sc.outerTrees(
                trees,
            )
            == output
        )
