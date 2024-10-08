import pytest
from q_1539_kthMissingPositiveNumber import Solution


@pytest.mark.parametrize(
    "arr, k, output", [([2, 3, 4, 7, 11], 5, 9), ([1, 2, 3, 4], 2, 6)]
)
class TestSolution:
    def test_findKthPositive(self, arr: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.findKthPositive(
                arr,
                k,
            )
            == output
        )
