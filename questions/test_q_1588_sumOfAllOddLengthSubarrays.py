import pytest
from q_1588_sumOfAllOddLengthSubarrays import Solution


@pytest.mark.parametrize(
    "arr, output", [([1, 4, 2, 5, 3], 58), ([1, 2], 3), ([10, 11, 12], 66)]
)
class TestSolution:
    def test_sumOddLengthSubarrays(self, arr: List[int], output: int):
        sc = Solution()
        assert (
            sc.sumOddLengthSubarrays(
                arr,
            )
            == output
        )
