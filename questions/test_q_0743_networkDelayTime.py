import pytest
from q_0743_networkDelayTime import Solution


@pytest.mark.parametrize(
    "times, n, k, output",
    [
        ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),
        ([[1, 2, 1]], 2, 1, 1),
        ([[1, 2, 1]], 2, 2, -1),
    ],
)
class TestSolution:
    def test_networkDelayTime(
        self, times: List[List[int]], n: int, k: int, output: int
    ):
        sc = Solution()
        assert (
            sc.networkDelayTime(
                times,
                n,
                k,
            )
            == output
        )
