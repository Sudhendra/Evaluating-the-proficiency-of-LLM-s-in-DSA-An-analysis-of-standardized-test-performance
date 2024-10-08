import pytest
from q_2616_minimizeTheMaximumDifferenceOfPairs import Solution


@pytest.mark.parametrize(
    "nums, p, output", [([10, 1, 2, 7, 1, 3], 2, 1), ([4, 2, 1, 2], 1, 0)]
)
class TestSolution:
    def test_minimizeMax(self, nums: List[int], p: int, output: int):
        sc = Solution()
        assert (
            sc.minimizeMax(
                nums,
                p,
            )
            == output
        )
