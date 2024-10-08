import pytest
from q_0912_sortAnArray import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([5, 2, 3, 1], [1, 2, 3, 5]), ([5, 1, 1, 2, 0, 0], [0, 0, 1, 1, 2, 5])],
)
class TestSolution:
    def test_sortArray(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.sortArray(
                nums,
            )
            == output
        )
