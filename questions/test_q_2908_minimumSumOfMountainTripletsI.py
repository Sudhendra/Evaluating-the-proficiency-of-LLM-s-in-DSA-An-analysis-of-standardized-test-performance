import pytest
from q_2908_minimumSumOfMountainTripletsI import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([8, 6, 1, 5, 3], 9), ([5, 4, 8, 7, 10, 2], 13), ([6, 5, 4, 3, 4, 5], -1)],
)
class TestSolution:
    def test_minimumSum(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimumSum(
                nums,
            )
            == output
        )
