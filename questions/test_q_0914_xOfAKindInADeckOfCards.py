import pytest
from q_0914_xOfAKindInADeckOfCards import Solution


@pytest.mark.parametrize(
    "deck, output",
    [([1, 2, 3, 4, 4, 3, 2, 1], True), ([1, 1, 1, 2, 2, 2, 3, 3], False)],
)
class TestSolution:
    def test_hasGroupsSizeX(self, deck: List[int], output: bool):
        sc = Solution()
        assert (
            sc.hasGroupsSizeX(
                deck,
            )
            == output
        )
