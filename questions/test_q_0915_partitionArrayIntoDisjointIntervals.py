import pytest
from q_0915_partitionArrayIntoDisjointIntervals import Solution


@pytest.mark.parametrize(
    "nums, output", [([5, 0, 3, 8, 6], 3), ([1, 1, 1, 0, 6, 12], 4)]
)
class TestSolution:
    def test_partitionDisjoint(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.partitionDisjoint(
                nums,
            )
            == output
        )
