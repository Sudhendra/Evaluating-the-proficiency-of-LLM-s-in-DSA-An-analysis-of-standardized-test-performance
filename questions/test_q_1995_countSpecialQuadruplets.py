import pytest
from q_1995_countSpecialQuadruplets import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 3, 6], 1), ([3, 3, 6, 4, 5], 0), ([1, 1, 1, 3, 5], 4)]
)
class TestSolution:
    def test_countQuadruplets(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.countQuadruplets(
                nums,
            )
            == output
        )
