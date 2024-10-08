import pytest
from q_2301_matchSubstringAfterReplacement import Solution


@pytest.mark.parametrize(
    "s, sub, mappings, output",
    [
        ("fool3e7bar", "leet", [["e", "3"], ["t", "7"], ["t", "8"]], True),
        ("fooleetbar", "f00l", [["o", "0"]], False),
        (
            "Fool33tbaR",
            "leetd",
            [["e", "3"], ["t", "7"], ["t", "8"], ["d", "b"], ["p", "b"]],
            True,
        ),
    ],
)
class TestSolution:
    def test_matchReplacement(
        self, s: str, sub: str, mappings: List[List[str]], output: bool
    ):
        sc = Solution()
        assert (
            sc.matchReplacement(
                s,
                sub,
                mappings,
            )
            == output
        )
