import pytest
from q_3046_splitTheArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 1, 2, 2, 3, 4], True), ([1, 1, 1, 1], False)]
)
class TestSolution:
    def test_isPossibleToSplit(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.isPossibleToSplit(
                nums,
            )
            == output
        )
