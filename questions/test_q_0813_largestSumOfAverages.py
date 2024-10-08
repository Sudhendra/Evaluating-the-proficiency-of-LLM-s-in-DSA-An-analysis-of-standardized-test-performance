import pytest
from q_0813_largestSumOfAverages import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([9, 1, 2, 3, 9], 3, 20.0), ([1, 2, 3, 4, 5, 6, 7], 4, 20.5)]
)
class TestSolution:
    def test_largestSumOfAverages(self, nums: List[int], k: int, output: float):
        sc = Solution()
        assert (
            sc.largestSumOfAverages(
                nums,
                k,
            )
            == output
        )
