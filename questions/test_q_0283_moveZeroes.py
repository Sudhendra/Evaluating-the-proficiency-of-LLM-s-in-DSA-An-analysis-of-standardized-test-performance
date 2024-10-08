import pytest
from q_0283_moveZeroes import Solution


@pytest.mark.parametrize(
    "nums, output", [([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]), ([0], [0])]
)
class TestSolution:
    def test_moveZeroes(self, nums: List[int], output: None):
        sc = Solution()
        assert (
            sc.moveZeroes(
                nums,
            )
            == output
        )
