import pytest
from q_0846_handOfStraights import Solution


@pytest.mark.parametrize(
    "hand, groupSize, output",
    [([1, 2, 3, 6, 2, 3, 4, 7, 8], 3, True), ([1, 2, 3, 4, 5], 4, False)],
)
class TestSolution:
    def test_isNStraightHand(self, hand: List[int], groupSize: int, output: bool):
        sc = Solution()
        assert (
            sc.isNStraightHand(
                hand,
                groupSize,
            )
            == output
        )
