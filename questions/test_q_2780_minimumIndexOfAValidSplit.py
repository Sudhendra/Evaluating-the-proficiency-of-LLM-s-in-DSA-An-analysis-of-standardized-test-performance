import pytest
from q_2780_minimumIndexOfAValidSplit import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([1, 2, 2, 2], 2),
        ([2, 1, 3, 1, 1, 1, 7, 1, 2, 1], 4),
        ([3, 3, 3, 3, 7, 2, 2], -1),
    ],
)
class TestSolution:
    def test_minimumIndex(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimumIndex(
                nums,
            )
            == output
        )
