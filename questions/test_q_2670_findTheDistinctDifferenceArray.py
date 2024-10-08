import pytest
from q_2670_findTheDistinctDifferenceArray import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([1, 2, 3, 4, 5], [-3, -1, 1, 3, 5]), ([3, 2, 3, 4, 2], [-2, -1, 0, 2, 3])],
)
class TestSolution:
    def test_distinctDifferenceArray(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.distinctDifferenceArray(
                nums,
            )
            == output
        )
