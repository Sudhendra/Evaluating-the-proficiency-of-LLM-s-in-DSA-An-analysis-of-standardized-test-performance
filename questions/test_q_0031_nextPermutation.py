import pytest
from q_0031_nextPermutation import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([1, 2, 3], [1, 3, 2]), ([3, 2, 1], [1, 2, 3]), ([1, 1, 5], [1, 5, 1])],
)
class TestSolution:
    def test_nextPermutation(self, nums: List[int], output: None):
        sc = Solution()
        assert (
            sc.nextPermutation(
                nums,
            )
            == output
        )
