import pytest
from q_2560_houseRobberIv import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([2, 3, 5, 9], 2, 5), ([2, 7, 9, 3, 1], 2, 2)]
)
class TestSolution:
    def test_minCapability(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.minCapability(
                nums,
                k,
            )
            == output
        )
