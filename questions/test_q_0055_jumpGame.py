import pytest
from q_0055_jumpGame import Solution


@pytest.mark.parametrize(
    "nums, output", [([2, 3, 1, 1, 4], True), ([3, 2, 1, 0, 4], False)]
)
class TestSolution:
    def test_canJump(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.canJump(
                nums,
            )
            == output
        )
