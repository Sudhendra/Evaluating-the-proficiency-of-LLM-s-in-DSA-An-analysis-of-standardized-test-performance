import pytest
from q_1686_stoneGameVi import Solution


@pytest.mark.parametrize(
    "aliceValues, bobValues, output",
    [([1, 3], [2, 1], 1), ([1, 2], [3, 1], 0), ([2, 4, 3], [1, 6, 7], -1)],
)
class TestSolution:
    def test_stoneGameVI(
        self, aliceValues: List[int], bobValues: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.stoneGameVI(
                aliceValues,
                bobValues,
            )
            == output
        )
