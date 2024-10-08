import pytest
from q_2347_bestPokerHand import Solution


@pytest.mark.parametrize(
    "ranks, suits, output",
    [
        ([13, 2, 3, 1, 9], ["a", "a", "a", "a", "a"], "Flush"),
        ([4, 4, 2, 4, 4], ["d", "a", "a", "b", "c"], "Three of a Kind"),
        ([10, 10, 2, 12, 9], ["a", "b", "c", "a", "d"], "Pair"),
    ],
)
class TestSolution:
    def test_bestHand(self, ranks: List[int], suits: List[str], output: str):
        sc = Solution()
        assert (
            sc.bestHand(
                ranks,
                suits,
            )
            == output
        )
