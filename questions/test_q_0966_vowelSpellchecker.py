import pytest
from q_0966_vowelSpellchecker import Solution


@pytest.mark.parametrize(
    "wordlist, queries, output",
    [
        (
            ["KiTe", "kite", "hare", "Hare"],
            [
                "kite",
                "Kite",
                "KiTe",
                "Hare",
                "HARE",
                "Hear",
                "hear",
                "keti",
                "keet",
                "keto",
            ],
            ["kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe"],
        ),
        (["yellow"], ["YellOw"], ["yellow"]),
    ],
)
class TestSolution:
    def test_spellchecker(
        self, wordlist: List[str], queries: List[str], output: List[str]
    ):
        sc = Solution()
        assert (
            sc.spellchecker(
                wordlist,
                queries,
            )
            == output
        )
