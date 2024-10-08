import pytest
from q_1000_minimumCostToMergeStones import Solution


@pytest.mark.parametrize(
    "stones, k, output",
    [([3, 2, 4, 1], 2, 20), ([3, 2, 4, 1], 3, -1), ([3, 5, 1, 2, 6], 3, 25)],
)
class TestSolution:
    def test_mergeStones(self, stones: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.mergeStones(
                stones,
                k,
            )
            == output
        )
