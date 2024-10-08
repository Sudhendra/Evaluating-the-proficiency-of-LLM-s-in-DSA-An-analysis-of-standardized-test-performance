import pytest
from q_1497_checkIfArrayPairsAreDivisibleByK import Solution


@pytest.mark.parametrize(
    "arr, k, output",
    [
        ([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5, True),
        ([1, 2, 3, 4, 5, 6], 7, True),
        ([1, 2, 3, 4, 5, 6], 10, False),
    ],
)
class TestSolution:
    def test_canArrange(self, arr: List[int], k: int, output: bool):
        sc = Solution()
        assert (
            sc.canArrange(
                arr,
                k,
            )
            == output
        )
