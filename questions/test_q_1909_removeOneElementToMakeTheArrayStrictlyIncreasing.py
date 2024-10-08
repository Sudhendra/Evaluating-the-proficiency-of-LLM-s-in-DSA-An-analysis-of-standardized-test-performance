import pytest
from q_1909_removeOneElementToMakeTheArrayStrictlyIncreasing import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([1, 2, 10, 5, 7], True), ([2, 3, 1, 2], False), ([1, 1, 1], False)],
)
class TestSolution:
    def test_canBeIncreasing(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.canBeIncreasing(
                nums,
            )
            == output
        )
