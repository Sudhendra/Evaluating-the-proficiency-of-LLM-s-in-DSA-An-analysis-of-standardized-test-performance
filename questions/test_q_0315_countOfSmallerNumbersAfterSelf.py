import pytest
from q_0315_countOfSmallerNumbersAfterSelf import Solution


@pytest.mark.parametrize(
    "nums, output", [([5, 2, 6, 1], [2, 1, 1, 0]), ([-1], [0]), ([-1, -1], [0, 0])]
)
class TestSolution:
    def test_countSmaller(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.countSmaller(
                nums,
            )
            == output
        )
