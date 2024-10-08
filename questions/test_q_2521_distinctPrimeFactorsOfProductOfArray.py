import pytest
from q_2521_distinctPrimeFactorsOfProductOfArray import Solution


@pytest.mark.parametrize("nums, output", [([2, 4, 3, 7, 10, 6], 4), ([2, 4, 8, 16], 1)])
class TestSolution:
    def test_distinctPrimeFactors(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.distinctPrimeFactors(
                nums,
            )
            == output
        )
