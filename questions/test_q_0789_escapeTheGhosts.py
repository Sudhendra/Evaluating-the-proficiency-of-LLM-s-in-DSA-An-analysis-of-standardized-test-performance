import pytest
from q_0789_escapeTheGhosts import Solution


@pytest.mark.parametrize(
    "ghosts, target, output",
    [
        ([[1, 0], [0, 3]], [0, 1], True),
        ([[1, 0]], [2, 0], False),
        ([[2, 0]], [1, 0], False),
    ],
)
class TestSolution:
    def test_escapeGhosts(
        self, ghosts: List[List[int]], target: List[int], output: bool
    ):
        sc = Solution()
        assert (
            sc.escapeGhosts(
                ghosts,
                target,
            )
            == output
        )
