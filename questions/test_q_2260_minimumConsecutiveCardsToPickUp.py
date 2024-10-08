import pytest
from q_2260_minimumConsecutiveCardsToPickUp import Solution


@pytest.mark.parametrize("cards, output", [([3, 4, 2, 3, 4, 7], 4), ([1, 0, 5, 3], -1)])
class TestSolution:
    def test_minimumCardPickup(self, cards: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimumCardPickup(
                cards,
            )
            == output
        )
