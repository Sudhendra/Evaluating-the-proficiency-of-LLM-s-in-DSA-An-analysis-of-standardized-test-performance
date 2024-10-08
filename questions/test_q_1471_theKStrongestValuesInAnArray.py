import pytest
from q_1471_theKStrongestValuesInAnArray import Solution


@pytest.mark.parametrize(
    "arr, k, output",
    [
        ([1, 2, 3, 4, 5], 2, [5, 1]),
        ([1, 1, 3, 5, 5], 2, [5, 5]),
        ([6, 7, 11, 7, 6, 8], 5, [11, 8, 6, 6, 7]),
    ],
)
class TestSolution:
    def test_getStrongest(self, arr: List[int], k: int, output: List[int]):
        sc = Solution()
        assert (
            sc.getStrongest(
                arr,
                k,
            )
            == output
        )
