import pytest
from q_2656_maximumSumWithExactlyKElements import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([1, 2, 3, 4, 5], 3, 18), ([5, 5, 5], 2, 11)]
)
class TestSolution:
    def test_maximizeSum(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.maximizeSum(
                nums,
                k,
            )
            == output
        )
