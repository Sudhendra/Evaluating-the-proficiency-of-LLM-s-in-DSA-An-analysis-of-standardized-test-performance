import pytest
from q_0162_findPeakElement import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 3, 1], 2), ([1, 2, 1, 3, 5, 6, 4], 5)]
)
class TestSolution:
    def test_findPeakElement(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.findPeakElement(
                nums,
            )
            == output
        )
