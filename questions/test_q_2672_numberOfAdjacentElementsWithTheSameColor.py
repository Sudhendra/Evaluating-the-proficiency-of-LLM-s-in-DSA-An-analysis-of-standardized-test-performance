import pytest
from q_2672_numberOfAdjacentElementsWithTheSameColor import Solution


@pytest.mark.parametrize(
    "n, queries, output",
    [
        (4, [[0, 2], [1, 2], [3, 1], [1, 1], [2, 1]], [0, 1, 1, 0, 2]),
        (1, [[0, 100000]], [0]),
    ],
)
class TestSolution:
    def test_colorTheArray(self, n: int, queries: List[List[int]], output: List[int]):
        sc = Solution()
        assert (
            sc.colorTheArray(
                n,
                queries,
            )
            == output
        )
