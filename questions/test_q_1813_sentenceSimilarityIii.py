import pytest
from q_1813_sentenceSimilarityIii import Solution


@pytest.mark.parametrize(
    "sentence1, sentence2, output",
    [
        ("My name is Haley", "My Haley", True),
        ("of", "A lot of words", False),
        ("Eating right now", "Eating", True),
    ],
)
class TestSolution:
    def test_areSentencesSimilar(self, sentence1: str, sentence2: str, output: bool):
        sc = Solution()
        assert (
            sc.areSentencesSimilar(
                sentence1,
                sentence2,
            )
            == output
        )
