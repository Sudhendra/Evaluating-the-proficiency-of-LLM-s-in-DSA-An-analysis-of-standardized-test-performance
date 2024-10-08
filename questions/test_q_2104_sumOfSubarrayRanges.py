import pytest
from q_2104_sumOfSubarrayRanges import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 3], 4), ([1, 3, 3], 4), ([4, -2, -3, 4, 1], 59)]
)
class TestSolution:
    def test_subArrayRanges(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.subArrayRanges(
                nums,
            )
            == output
        )
