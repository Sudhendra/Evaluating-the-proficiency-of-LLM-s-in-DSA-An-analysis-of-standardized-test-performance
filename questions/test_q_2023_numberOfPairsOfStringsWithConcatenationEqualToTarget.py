import pytest
from q_2023_numberOfPairsOfStringsWithConcatenationEqualToTarget import Solution


@pytest.mark.parametrize(
    "nums, target, output",
    [
        (["777", "7", "77", "77"], "7777", 4),
        (["123", "4", "12", "34"], "1234", 2),
        (["1", "1", "1"], "11", 6),
    ],
)
class TestSolution:
    def test_numOfPairs(self, nums: List[str], target: str, output: int):
        sc = Solution()
        assert (
            sc.numOfPairs(
                nums,
                target,
            )
            == output
        )
