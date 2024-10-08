import pytest
from q_0744_findSmallestLetterGreaterThanTarget import Solution


@pytest.mark.parametrize(
    "letters, target, output",
    [
        (["c", "f", "j"], "a", "c"),
        (["c", "f", "j"], "c", "f"),
        (["x", "x", "y", "y"], "z", "x"),
    ],
)
class TestSolution:
    def test_nextGreatestLetter(self, letters: List[str], target: str, output: str):
        sc = Solution()
        assert (
            sc.nextGreatestLetter(
                letters,
                target,
            )
            == output
        )
