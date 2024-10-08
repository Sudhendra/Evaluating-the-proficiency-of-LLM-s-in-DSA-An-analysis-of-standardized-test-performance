import pytest
from q_2612_minimumReverseOperations import Solution


@pytest.mark.parametrize(
    "n, p, banned, k, output",
    [
        (4, 0, [1, 2], 4, [0, -1, -1, 1]),
        (5, 0, [2, 4], 3, [0, -1, -1, -1, -1]),
        (4, 2, [0, 1, 3], 1, [-1, -1, 0, -1]),
    ],
)
class TestSolution:
    def test_minReverseOperations(
        self, n: int, p: int, banned: List[int], k: int, output: List[int]
    ):
        sc = Solution()
        assert (
            sc.minReverseOperations(
                n,
                p,
                banned,
                k,
            )
            == output
        )
