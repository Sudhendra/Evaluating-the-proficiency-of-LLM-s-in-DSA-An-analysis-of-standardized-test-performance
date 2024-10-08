import pytest
from q_0628_maximumProductOfThreeNumbers import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 3], 6), ([1, 2, 3, 4], 24), ([-1, -2, -3], -6)]
)
class TestSolution:
    def test_maximumProduct(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maximumProduct(
                nums,
            )
            == output
        )
