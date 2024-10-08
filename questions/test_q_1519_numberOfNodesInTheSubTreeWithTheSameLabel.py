import pytest
from q_1519_numberOfNodesInTheSubTreeWithTheSameLabel import Solution


@pytest.mark.parametrize(
    "n, edges, labels, output",
    [
        (
            7,
            [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            "abaedcd",
            [2, 1, 1, 1, 1, 1, 1],
        ),
        (4, [[0, 1], [1, 2], [0, 3]], "bbbb", [4, 2, 1, 1]),
        (5, [[0, 1], [0, 2], [1, 3], [0, 4]], "aabab", [3, 2, 1, 1, 1]),
    ],
)
class TestSolution:
    def test_countSubTrees(
        self, n: int, edges: List[List[int]], labels: str, output: List[int]
    ):
        sc = Solution()
        assert (
            sc.countSubTrees(
                n,
                edges,
                labels,
            )
            == output
        )
