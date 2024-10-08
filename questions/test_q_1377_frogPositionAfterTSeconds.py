import pytest
from q_1377_frogPositionAfterTSeconds import Solution


@pytest.mark.parametrize(
    "n, edges, t, target, output",
    [
        (
            7,
            [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]],
            2,
            4,
            0.16666666666666666,
        ),
        (7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 1, 7, 0.3333333333333333),
    ],
)
class TestSolution:
    def test_frogPosition(
        self, n: int, edges: List[List[int]], t: int, target: int, output: float
    ):
        sc = Solution()
        assert (
            sc.frogPosition(
                n,
                edges,
                t,
                target,
            )
            == output
        )
