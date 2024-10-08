import pytest
from q_2134_minimumSwapsToGroupAll1STogetherIi import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([0, 1, 0, 1, 1, 0, 0], 1),
        ([0, 1, 1, 1, 0, 0, 1, 1, 0], 2),
        ([1, 1, 0, 0, 1], 0),
    ],
)
class TestSolution:
    def test_minSwaps(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minSwaps(
                nums,
            )
            == output
        )
