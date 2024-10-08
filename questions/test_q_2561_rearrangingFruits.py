import pytest
from q_2561_rearrangingFruits import Solution


@pytest.mark.parametrize(
    "basket1, basket2, output",
    [([4, 2, 2, 2], [1, 4, 1, 2], 1), ([2, 3, 4, 1], [3, 2, 5, 1], -1)],
)
class TestSolution:
    def test_minCost(self, basket1: List[int], basket2: List[int], output: int):
        sc = Solution()
        assert (
            sc.minCost(
                basket1,
                basket2,
            )
            == output
        )
