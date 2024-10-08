import pytest
from q_1406_stoneGameIii import Solution


@pytest.mark.parametrize(
    "stoneValue, output",
    [([1, 2, 3, 7], "Bob"), ([1, 2, 3, -9], "Alice"), ([1, 2, 3, 6], "Tie")],
)
class TestSolution:
    def test_stoneGameIII(self, stoneValue: List[int], output: str):
        sc = Solution()
        assert (
            sc.stoneGameIII(
                stoneValue,
            )
            == output
        )
