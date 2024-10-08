import pytest
from q_1862_sumOfFlooredPairs import Solution


@pytest.mark.parametrize("nums, output", [([2, 5, 9], 10), ([7, 7, 7, 7, 7, 7, 7], 49)])
class TestSolution:
    def test_sumOfFlooredPairs(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.sumOfFlooredPairs(
                nums,
            )
            == output
        )
