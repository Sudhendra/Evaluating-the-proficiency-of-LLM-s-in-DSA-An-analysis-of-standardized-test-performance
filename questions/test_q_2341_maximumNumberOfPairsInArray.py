import pytest
from q_2341_maximumNumberOfPairsInArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 3, 2, 1, 3, 2, 2], [3, 1]), ([1, 1], [1, 0]), ([0], [0, 1])]
)
class TestSolution:
    def test_numberOfPairs(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.numberOfPairs(
                nums,
            )
            == output
        )
