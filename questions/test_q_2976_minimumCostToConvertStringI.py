import pytest
from q_2976_minimumCostToConvertStringI import Solution


@pytest.mark.parametrize(
    "source, target, original, changed, cost, output",
    [
        (
            "abcd",
            "acbe",
            ["a", "b", "c", "c", "e", "d"],
            ["b", "c", "b", "e", "b", "e"],
            [2, 5, 5, 1, 2, 20],
            28,
        ),
        ("aaaa", "bbbb", ["a", "c"], ["c", "b"], [1, 2], 12),
        ("abcd", "abce", ["a"], ["e"], [10000], -1),
    ],
)
class TestSolution:
    def test_minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
        output: int,
    ):
        sc = Solution()
        assert (
            sc.minimumCost(
                source,
                target,
                original,
                changed,
                cost,
            )
            == output
        )
