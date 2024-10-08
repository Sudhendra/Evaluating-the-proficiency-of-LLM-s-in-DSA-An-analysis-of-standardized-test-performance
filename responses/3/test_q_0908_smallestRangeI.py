from typing import List
import pytest
from q_0908_smallestRangeI import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([1], 0, 0), ([0, 10], 2, 6), ([1, 3, 6], 3, 0)]
)
class TestSolution:
    def test_smallestRangeI(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.smallestRangeI(
                nums,
                k,
            )
            == output
        )
