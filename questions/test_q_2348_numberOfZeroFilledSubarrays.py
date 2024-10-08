import pytest
from q_2348_numberOfZeroFilledSubarrays import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([1, 3, 0, 0, 2, 0, 0, 4], 6), ([0, 0, 0, 2, 0, 0], 9), ([2, 10, 2019], 0)],
)
class TestSolution:
    def test_zeroFilledSubarray(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.zeroFilledSubarray(
                nums,
            )
            == output
        )
