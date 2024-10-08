import pytest
from q_2057_smallestIndexWithEqualValue import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([0, 1, 2], 0), ([4, 3, 2, 1], 2), ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], -1)],
)
class TestSolution:
    def test_smallestEqual(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.smallestEqual(
                nums,
            )
            == output
        )
