import pytest
from q_0287_findTheDuplicateNumber import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 3, 4, 2, 2], 2), ([3, 1, 3, 4, 2], 3), ([3, 3, 3, 3, 3], 3)]
)
class TestSolution:
    def test_findDuplicate(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.findDuplicate(
                nums,
            )
            == output
        )
