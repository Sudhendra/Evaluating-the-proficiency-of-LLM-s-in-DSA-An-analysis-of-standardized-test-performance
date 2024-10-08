import pytest
from q_2242_maximumScoreOfANodeSequence import Solution


@pytest.mark.parametrize(
    "scores, edges, output",
    [
        ([5, 2, 9, 8, 4], [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]], 24),
        ([9, 20, 6, 4, 11, 12], [[0, 3], [5, 3], [2, 4], [1, 3]], -1),
    ],
)
class TestSolution:
    def test_maximumScore(self, scores: List[int], edges: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maximumScore(
                scores,
                edges,
            )
            == output
        )
