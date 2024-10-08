import pytest
from q_2202_maximizeTheTopmostElementAfterKMoves import Solution


@pytest.mark.parametrize("nums, k, output", [([5, 2, 2, 4, 0, 6], 4, 5), ([2], 1, -1)])
class TestSolution:
    def test_maximumTop(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.maximumTop(
                nums,
                k,
            )
            == output
        )
