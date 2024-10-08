import pytest
from q_2216_minimumDeletionsToMakeArrayBeautiful import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 1, 2, 3, 5], 1), ([1, 1, 2, 2, 3, 3], 2)]
)
class TestSolution:
    def test_minDeletion(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minDeletion(
                nums,
            )
            == output
        )
