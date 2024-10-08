import pytest
from q_1514_pathWithMaximumProbability import Solution


@pytest.mark.parametrize(
    "n, edges, succProb, start, end, output",
    [
        (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2, 0.25),
        (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2, 0.3),
        (3, [[0, 1]], [0.5], 0, 2, 0.0),
    ],
)
class TestSolution:
    def test_maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
        output: float,
    ):
        sc = Solution()
        assert (
            sc.maxProbability(
                n,
                edges,
                succProb,
                start,
                end,
            )
            == output
        )
