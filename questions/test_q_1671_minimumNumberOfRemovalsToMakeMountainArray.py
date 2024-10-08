import pytest
from q_1671_minimumNumberOfRemovalsToMakeMountainArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 3, 1], 0), ([2, 1, 1, 5, 6, 2, 3, 1], 3)]
)
class TestSolution:
    def test_minimumMountainRemovals(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimumMountainRemovals(
                nums,
            )
            == output
        )
