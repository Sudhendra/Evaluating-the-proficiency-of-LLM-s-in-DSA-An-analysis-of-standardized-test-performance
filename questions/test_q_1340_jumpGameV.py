import pytest
from q_1340_jumpGameV import Solution


@pytest.mark.parametrize(
    "arr, d, output",
    [
        ([6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], 2, 4),
        ([3, 3, 3, 3, 3], 3, 1),
        ([7, 6, 5, 4, 3, 2, 1], 1, 7),
    ],
)
class TestSolution:
    def test_maxJumps(self, arr: List[int], d: int, output: int):
        sc = Solution()
        assert (
            sc.maxJumps(
                arr,
                d,
            )
            == output
        )
