import pytest
from q_2161_partitionArrayAccordingToGivenPivot import Solution


@pytest.mark.parametrize(
    "nums, pivot, output",
    [
        ([9, 12, 5, 10, 14, 3, 10], 10, [9, 5, 3, 10, 10, 12, 14]),
        ([-3, 4, 3, 2], 2, [-3, 2, 4, 3]),
    ],
)
class TestSolution:
    def test_pivotArray(self, nums: List[int], pivot: int, output: List[int]):
        sc = Solution()
        assert (
            sc.pivotArray(
                nums,
                pivot,
            )
            == output
        )
