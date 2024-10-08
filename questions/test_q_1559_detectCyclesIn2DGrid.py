import pytest
from q_1559_detectCyclesIn2DGrid import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        (
            [
                ["a", "a", "a", "a"],
                ["a", "b", "b", "a"],
                ["a", "b", "b", "a"],
                ["a", "a", "a", "a"],
            ],
            True,
        ),
        (
            [
                ["c", "c", "c", "a"],
                ["c", "d", "c", "c"],
                ["c", "c", "e", "c"],
                ["f", "c", "c", "c"],
            ],
            True,
        ),
        ([["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]], False),
    ],
)
class TestSolution:
    def test_containsCycle(self, grid: List[List[str]], output: bool):
        sc = Solution()
        assert (
            sc.containsCycle(
                grid,
            )
            == output
        )
