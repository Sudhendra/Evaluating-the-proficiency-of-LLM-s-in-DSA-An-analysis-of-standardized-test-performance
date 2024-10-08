import pytest
from q_2581_countNumberOfPossibleRootNodes import Solution


@pytest.mark.parametrize(
    "edges, guesses, k, output",
    [
        ([[0, 1], [1, 2], [1, 3], [4, 2]], [[1, 3], [0, 1], [1, 0], [2, 4]], 3, 3),
        ([[0, 1], [1, 2], [2, 3], [3, 4]], [[1, 0], [3, 4], [2, 1], [3, 2]], 1, 5),
    ],
)
class TestSolution:
    def test_rootCount(
        self, edges: List[List[int]], guesses: List[List[int]], k: int, output: int
    ):
        sc = Solution()
        assert (
            sc.rootCount(
                edges,
                guesses,
                k,
            )
            == output
        )
