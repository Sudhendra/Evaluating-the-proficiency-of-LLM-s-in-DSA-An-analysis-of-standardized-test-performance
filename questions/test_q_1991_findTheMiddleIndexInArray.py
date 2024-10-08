import pytest
from q_1991_findTheMiddleIndexInArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([2, 3, -1, 8, 4], 3), ([1, -1, 4], 2), ([2, 5], -1)]
)
class TestSolution:
    def test_findMiddleIndex(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.findMiddleIndex(
                nums,
            )
            == output
        )
