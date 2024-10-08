import pytest
from q_1578_minimumTimeToMakeRopeColorful import Solution


@pytest.mark.parametrize(
    "colors, neededTime, output",
    [
        ("abaac", [1, 2, 3, 4, 5], 3),
        ("abc", [1, 2, 3], 0),
        ("aabaa", [1, 2, 3, 4, 1], 2),
    ],
)
class TestSolution:
    def test_minCost(self, colors: str, neededTime: List[int], output: int):
        sc = Solution()
        assert (
            sc.minCost(
                colors,
                neededTime,
            )
            == output
        )
