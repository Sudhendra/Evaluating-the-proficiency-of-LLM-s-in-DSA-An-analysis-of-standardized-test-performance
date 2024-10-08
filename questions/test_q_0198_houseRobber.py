import pytest
from q_0198_houseRobber import Solution


@pytest.mark.parametrize("nums, output", [([1, 2, 3, 1], 4), ([2, 7, 9, 3, 1], 12)])
class TestSolution:
    def test_rob(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.rob(
                nums,
            )
            == output
        )
