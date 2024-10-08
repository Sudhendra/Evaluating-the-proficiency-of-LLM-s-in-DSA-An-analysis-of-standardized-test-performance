import pytest
from q_1606_findServersThatHandledMostNumberOfRequests import Solution


@pytest.mark.parametrize(
    "k, arrival, load, output",
    [
        (3, [1, 2, 3, 4, 5], [5, 2, 3, 3, 3], [1]),
        (3, [1, 2, 3, 4], [1, 2, 1, 2], [0]),
        (3, [1, 2, 3], [10, 12, 11], [0, 1, 2]),
    ],
)
class TestSolution:
    def test_busiestServers(
        self, k: int, arrival: List[int], load: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.busiestServers(
                k,
                arrival,
                load,
            )
            == output
        )
