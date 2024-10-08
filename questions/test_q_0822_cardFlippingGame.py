import pytest
from q_0822_cardFlippingGame import Solution


@pytest.mark.parametrize(
    "fronts, backs, output", [([1, 2, 4, 4, 7], [1, 3, 4, 1, 3], 2), ([1], [1], 0)]
)
class TestSolution:
    def test_flipgame(self, fronts: List[int], backs: List[int], output: int):
        sc = Solution()
        assert (
            sc.flipgame(
                fronts,
                backs,
            )
            == output
        )
