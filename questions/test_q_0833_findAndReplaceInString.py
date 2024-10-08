import pytest
from q_0833_findAndReplaceInString import Solution


@pytest.mark.parametrize(
    "s, indices, sources, targets, output",
    [
        ("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"], "eeebffff"),
        ("abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"], "eeecd"),
    ],
)
class TestSolution:
    def test_findReplaceString(
        self,
        s: str,
        indices: List[int],
        sources: List[str],
        targets: List[str],
        output: str,
    ):
        sc = Solution()
        assert (
            sc.findReplaceString(
                s,
                indices,
                sources,
                targets,
            )
            == output
        )
