import pytest
from q_0506_relativeRanks import Solution


@pytest.mark.parametrize(
    "score, output",
    [
        ([5, 4, 3, 2, 1], ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]),
        ([10, 3, 8, 9, 4], ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]),
    ],
)
class TestSolution:
    def test_findRelativeRanks(self, score: List[int], output: List[str]):
        sc = Solution()
        assert (
            sc.findRelativeRanks(
                score,
            )
            == output
        )
