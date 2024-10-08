import pytest
from q_2300_successfulPairsOfSpellsAndPotions import Solution


@pytest.mark.parametrize(
    "spells, potions, success, output",
    [([5, 1, 3], [1, 2, 3, 4, 5], 7, [4, 0, 3]), ([3, 1, 2], [8, 5, 8], 16, [2, 0, 2])],
)
class TestSolution:
    def test_successfulPairs(
        self, spells: List[int], potions: List[int], success: int, output: List[int]
    ):
        sc = Solution()
        assert (
            sc.successfulPairs(
                spells,
                potions,
                success,
            )
            == output
        )
