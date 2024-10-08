import pytest
from q_1186_maximumSubarraySumWithOneDeletion import Solution


@pytest.mark.parametrize(
    "arr, output", [([1, -2, 0, 3], 4), ([1, -2, -2, 3], 3), ([-1, -1, -1, -1], -1)]
)
class TestSolution:
    def test_maximumSum(self, arr: List[int], output: int):
        sc = Solution()
        assert (
            sc.maximumSum(
                arr,
            )
            == output
        )
