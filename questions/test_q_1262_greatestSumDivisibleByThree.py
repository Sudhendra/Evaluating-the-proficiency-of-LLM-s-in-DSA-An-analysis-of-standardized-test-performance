import pytest
from q_1262_greatestSumDivisibleByThree import Solution


@pytest.mark.parametrize(
    "nums, output", [([3, 6, 5, 1, 8], 18), ([4], 0), ([1, 2, 3, 4, 4], 12)]
)
class TestSolution:
    def test_maxSumDivThree(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxSumDivThree(
                nums,
            )
            == output
        )
