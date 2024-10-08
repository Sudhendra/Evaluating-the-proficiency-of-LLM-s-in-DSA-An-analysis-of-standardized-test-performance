import pytest
from q_0090_subsetsIi import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]), ([0], [[], [0]])],
)
class TestSolution:
    def test_subsetsWithDup(self, nums: List[int], output: List[List[int]]):
        sc = Solution()
        assert (
            sc.subsetsWithDup(
                nums,
            )
            == output
        )
