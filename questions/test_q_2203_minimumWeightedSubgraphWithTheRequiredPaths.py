import pytest
from q_2203_minimumWeightedSubgraphWithTheRequiredPaths import Solution


@pytest.mark.parametrize(
    "n, edges, src1, src2, dest, output",
    [
        (
            6,
            [
                [0, 2, 2],
                [0, 5, 6],
                [1, 0, 3],
                [1, 4, 5],
                [2, 1, 1],
                [2, 3, 3],
                [2, 3, 4],
                [3, 4, 2],
                [4, 5, 1],
            ],
            0,
            1,
            5,
            9,
        ),
        (3, [[0, 1, 1], [2, 1, 1]], 0, 1, 2, -1),
    ],
)
class TestSolution:
    def test_minimumWeight(
        self,
        n: int,
        edges: List[List[int]],
        src1: int,
        src2: int,
        dest: int,
        output: int,
    ):
        sc = Solution()
        assert (
            sc.minimumWeight(
                n,
                edges,
                src1,
                src2,
                dest,
            )
            == output
        )
