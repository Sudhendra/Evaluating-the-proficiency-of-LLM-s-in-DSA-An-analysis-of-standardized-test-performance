import pytest
from q_0523_continuousSubarraySum import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [
        ([23, 2, 4, 6, 7], 6, True),
        ([23, 2, 6, 4, 7], 6, True),
        ([23, 2, 6, 4, 7], 13, False),
    ],
)
class TestSolution:
    def test_checkSubarraySum(self, nums: List[int], k: int, output: bool):
        sc = Solution()
        assert (
            sc.checkSubarraySum(
                nums,
                k,
            )
            == output
        )
