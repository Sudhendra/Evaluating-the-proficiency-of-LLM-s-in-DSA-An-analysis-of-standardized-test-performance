import pytest
from q_0472_concatenatedWords import Solution


@pytest.mark.parametrize(
    "words, output",
    [
        (
            [
                "cat",
                "cats",
                "catsdogcats",
                "dog",
                "dogcatsdog",
                "hippopotamuses",
                "rat",
                "ratcatdogcat",
            ],
            ["catsdogcats", "dogcatsdog", "ratcatdogcat"],
        ),
        (["cat", "dog", "catdog"], ["catdog"]),
    ],
)
class TestSolution:
    def test_findAllConcatenatedWordsInADict(self, words: List[str], output: List[str]):
        sc = Solution()
        assert (
            sc.findAllConcatenatedWordsInADict(
                words,
            )
            == output
        )
