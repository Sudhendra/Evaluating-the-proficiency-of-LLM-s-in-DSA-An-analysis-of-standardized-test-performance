import pytest
from q_0632_smallestRangeCoveringElementsFromKLists import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]], [20, 24]),
        ([[1, 2, 3], [1, 2, 3], [1, 2, 3]], [1, 1]),
    ],
)
class TestSolution:
    def test_smallestRange(self, nums: List[List[int]], output: List[int]):
        sc = Solution()
        assert (
            sc.smallestRange(
                nums,
            )
            == output
        )
