import pytest
from q_2267_checkIfThereIsAValidParenthesesStringPath import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([["(", "(", "("], [")", "(", ")"], ["(", "(", ")"], ["(", "(", ")"]], True),
        ([[")", ")"], ["(", "("]], False),
    ],
)
class TestSolution:
    def test_hasValidPath(self, grid: List[List[str]], output: bool):
        sc = Solution()
        assert (
            sc.hasValidPath(
                grid,
            )
            == output
        )
