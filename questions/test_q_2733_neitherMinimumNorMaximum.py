import pytest
from q_2733_neitherMinimumNorMaximum import Solution


@pytest.mark.parametrize(
    "nums, output", [([3, 2, 1, 4], 2), ([1, 2], -1), ([2, 1, 3], 2)]
)
class TestSolution:
    def test_findNonMinOrMax(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.findNonMinOrMax(
                nums,
            )
            == output
        )
