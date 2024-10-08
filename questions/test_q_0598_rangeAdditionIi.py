import pytest
from q_0598_rangeAdditionIi import Solution


@pytest.mark.parametrize(
    "m, n, ops, output",
    [
        (3, 3, [[2, 2], [3, 3]], 4),
        (
            3,
            3,
            [
                [2, 2],
                [3, 3],
                [3, 3],
                [3, 3],
                [2, 2],
                [3, 3],
                [3, 3],
                [3, 3],
                [2, 2],
                [3, 3],
                [3, 3],
                [3, 3],
            ],
            4,
        ),
        (3, 3, [], 9),
    ],
)
class TestSolution:
    def test_maxCount(self, m: int, n: int, ops: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maxCount(
                m,
                n,
                ops,
            )
            == output
        )
