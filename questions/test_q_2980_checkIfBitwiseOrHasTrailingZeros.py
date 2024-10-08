import pytest
from q_2980_checkIfBitwiseOrHasTrailingZeros import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([1, 2, 3, 4, 5], True), ([2, 4, 8, 16], True), ([1, 3, 5, 7, 9], False)],
)
class TestSolution:
    def test_hasTrailingZeros(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.hasTrailingZeros(
                nums,
            )
            == output
        )
