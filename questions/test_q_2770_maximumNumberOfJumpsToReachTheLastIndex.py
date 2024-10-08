import pytest
from q_2770_maximumNumberOfJumpsToReachTheLastIndex import Solution


@pytest.mark.parametrize(
    "nums, target, output",
    [
        ([1, 3, 6, 4, 1, 2], 2, 3),
        ([1, 3, 6, 4, 1, 2], 3, 5),
        ([1, 3, 6, 4, 1, 2], 0, -1),
    ],
)
class TestSolution:
    def test_maximumJumps(self, nums: List[int], target: int, output: int):
        sc = Solution()
        assert (
            sc.maximumJumps(
                nums,
                target,
            )
            == output
        )
