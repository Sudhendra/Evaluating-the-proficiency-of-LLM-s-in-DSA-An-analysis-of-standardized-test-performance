import pytest
from q_0907_sumOfSubarrayMinimums import Solution


@pytest.mark.parametrize(
    "arr, output", [([3, 1, 2, 4], 17), ([11, 81, 94, 43, 3], 444)]
)
class TestSolution:
    def test_sumSubarrayMins(self, arr: List[int], output: int):
        sc = Solution()
        assert (
            sc.sumSubarrayMins(
                arr,
            )
            == output
        )
