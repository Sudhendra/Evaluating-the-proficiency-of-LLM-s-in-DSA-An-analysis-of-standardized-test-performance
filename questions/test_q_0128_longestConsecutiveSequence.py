import pytest
from q_0128_longestConsecutiveSequence import Solution


@pytest.mark.parametrize(
    "nums, output", [([100, 4, 200, 1, 3, 2], 4), ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9)]
)
class TestSolution:
    def test_longestConsecutive(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.longestConsecutive(
                nums,
            )
            == output
        )
