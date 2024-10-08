import pytest
from q_1974_minimumTimeToTypeWordUsingSpecialTypewriter import Solution


@pytest.mark.parametrize("word, output", [("abc", 5), ("bza", 7), ("zjpc", 34)])
class TestSolution:
    def test_minTimeToType(self, word: str, output: int):
        sc = Solution()
        assert (
            sc.minTimeToType(
                word,
            )
            == output
        )
