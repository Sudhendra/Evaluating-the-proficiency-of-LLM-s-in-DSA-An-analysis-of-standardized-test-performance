import pytest
from q_0238_productOfArrayExceptSelf import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([1, 2, 3, 4], [24, 12, 8, 6]), ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0])],
)
class TestSolution:
    def test_productExceptSelf(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.productExceptSelf(
                nums,
            )
            == output
        )
