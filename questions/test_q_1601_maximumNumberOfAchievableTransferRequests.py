import pytest
from q_1601_maximumNumberOfAchievableTransferRequests import Solution


@pytest.mark.parametrize(
    "n, requests, output",
    [
        (5, [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]], 5),
        (3, [[0, 0], [1, 2], [2, 1]], 3),
        (4, [[0, 3], [3, 1], [1, 2], [2, 0]], 4),
    ],
)
class TestSolution:
    def test_maximumRequests(self, n: int, requests: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maximumRequests(
                n,
                requests,
            )
            == output
        )
