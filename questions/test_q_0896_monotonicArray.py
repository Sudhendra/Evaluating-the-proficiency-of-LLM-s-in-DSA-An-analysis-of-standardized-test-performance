import pytest
from q_0896_monotonicArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 2, 3], True), ([6, 5, 4, 4], True), ([1, 3, 2], False)]
)
class TestSolution:
    def test_isMonotonic(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.isMonotonic(
                nums,
            )
            == output
        )
