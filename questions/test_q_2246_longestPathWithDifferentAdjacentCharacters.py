import pytest
from q_2246_longestPathWithDifferentAdjacentCharacters import Solution


@pytest.mark.parametrize(
    "parent, s, output",
    [([-1, 0, 0, 1, 1, 2], "abacbe", 3), ([-1, 0, 0, 0], "aabc", 3)],
)
class TestSolution:
    def test_longestPath(self, parent: List[int], s: str, output: int):
        sc = Solution()
        assert (
            sc.longestPath(
                parent,
                s,
            )
            == output
        )
