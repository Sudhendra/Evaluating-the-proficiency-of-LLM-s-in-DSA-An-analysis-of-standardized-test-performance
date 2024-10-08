import pytest
from q_3005_countElementsWithMaximumFrequency import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 2, 3, 1, 4], 4), ([1, 2, 3, 4, 5], 5)]
)
class TestSolution:
    def test_maxFrequencyElements(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxFrequencyElements(
                nums,
            )
            == output
        )
