import pytest
from q_1748_sumOfUniqueElements import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 3, 2], 4), ([1, 1, 1, 1, 1], 0), ([1, 2, 3, 4, 5], 15)]
)
class TestSolution:
    def test_sumOfUnique(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.sumOfUnique(
                nums,
            )
            == output
        )
