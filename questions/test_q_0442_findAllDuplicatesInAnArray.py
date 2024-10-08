import pytest
from q_0442_findAllDuplicatesInAnArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([4, 3, 2, 7, 8, 2, 3, 1], [2, 3]), ([1, 1, 2], [1]), ([1], [])]
)
class TestSolution:
    def test_findDuplicates(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.findDuplicates(
                nums,
            )
            == output
        )
