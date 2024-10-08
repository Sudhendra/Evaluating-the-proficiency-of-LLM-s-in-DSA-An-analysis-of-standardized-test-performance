import pytest
from q_2270_numberOfWaysToSplitArray import Solution


@pytest.mark.parametrize("nums, output", [([10, 4, -8, 7], 2), ([2, 3, 1, 0], 2)])
class TestSolution:
    def test_waysToSplitArray(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.waysToSplitArray(
                nums,
            )
            == output
        )
