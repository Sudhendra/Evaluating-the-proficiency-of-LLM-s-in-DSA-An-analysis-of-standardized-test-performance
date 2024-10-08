import pytest
from q_0945_minimumIncrementToMakeArrayUnique import Solution


@pytest.mark.parametrize("nums, output", [([1, 2, 2], 1), ([3, 2, 1, 2, 1, 7], 6)])
class TestSolution:
    def test_minIncrementForUnique(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minIncrementForUnique(
                nums,
            )
            == output
        )
