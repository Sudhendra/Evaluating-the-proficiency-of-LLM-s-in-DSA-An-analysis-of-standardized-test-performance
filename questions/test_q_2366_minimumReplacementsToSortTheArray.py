import pytest
from q_2366_minimumReplacementsToSortTheArray import Solution


@pytest.mark.parametrize("nums, output", [([3, 9, 3], 2), ([1, 2, 3, 4, 5], 0)])
class TestSolution:
    def test_minimumReplacement(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimumReplacement(
                nums,
            )
            == output
        )
