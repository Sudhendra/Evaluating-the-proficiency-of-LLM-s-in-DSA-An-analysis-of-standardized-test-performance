import pytest
from q_3014_minimumNumberOfPushesToTypeWordI import Solution


@pytest.mark.parametrize("word, output", [("abcde", 5), ("xycdefghij", 12)])
class TestSolution:
    def test_minimumPushes(self, word: str, output: int):
        sc = Solution()
        assert (
            sc.minimumPushes(
                word,
            )
            == output
        )
