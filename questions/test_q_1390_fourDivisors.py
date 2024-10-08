import pytest
from q_1390_fourDivisors import Solution


@pytest.mark.parametrize(
    "nums, output", [([21, 4, 7], 32), ([21, 21], 64), ([1, 2, 3, 4, 5], 0)]
)
class TestSolution:
    def test_sumFourDivisors(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.sumFourDivisors(
                nums,
            )
            == output
        )
