import pytest
from q_3031_minimumTimeToRevertWordToInitialStateIi import Solution


@pytest.mark.parametrize(
    "word, k, output", [("abacaba", 3, 2), ("abacaba", 4, 1), ("abcbabcd", 2, 4)]
)
class TestSolution:
    def test_minimumTimeToInitialState(self, word: str, k: int, output: int):
        sc = Solution()
        assert (
            sc.minimumTimeToInitialState(
                word,
                k,
            )
            == output
        )
