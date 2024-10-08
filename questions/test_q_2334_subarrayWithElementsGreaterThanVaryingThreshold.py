import pytest
from q_2334_subarrayWithElementsGreaterThanVaryingThreshold import Solution


@pytest.mark.parametrize(
    "nums, threshold, output", [([1, 3, 4, 3, 1], 6, 3), ([6, 5, 6, 5, 8], 7, 1)]
)
class TestSolution:
    def test_validSubarraySize(self, nums: List[int], threshold: int, output: int):
        sc = Solution()
        assert (
            sc.validSubarraySize(
                nums,
                threshold,
            )
            == output
        )
