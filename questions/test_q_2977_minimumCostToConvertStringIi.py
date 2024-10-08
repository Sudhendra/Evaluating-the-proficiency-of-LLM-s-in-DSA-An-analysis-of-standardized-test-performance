import pytest
from q_2977_minimumCostToConvertStringIi import Solution


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
        (
            "abcdefgh",
            "acdeeghh",
            ["bcd", "fgh", "thh"],
            ["cde", "thh", "ghh"],
            [1, 3, 5],
            9,
        ),
        ("abcdefgh", "addddddd", ["bcd", "defgh"], ["ddd", "ddddd"], [100, 1578], -1),
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
