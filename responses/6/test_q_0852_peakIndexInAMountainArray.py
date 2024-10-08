from typing import List
import pytest
from q_0852_peakIndexInAMountainArray import Solution


@pytest.mark.parametrize(
    "arr, output", [([0, 1, 0], 1), ([0, 2, 1, 0], 1), ([0, 10, 5, 2], 1)]
)
class TestSolution:
    def test_peakIndexInMountainArray(self, arr: List[int], output: int):
        sc = Solution()
        assert (
            sc.peakIndexInMountainArray(
                arr,
            )
            == output
        )
