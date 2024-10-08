import pytest
from q_1768_mergeStringsAlternately import Solution


@pytest.mark.parametrize(
    "word1, word2, output",
    [("abc", "pqr", "apbqcr"), ("ab", "pqrs", "apbqrs"), ("abcd", "pq", "apbqcd")],
)
class TestSolution:
    def test_mergeAlternately(self, word1: str, word2: str, output: str):
        sc = Solution()
        assert (
            sc.mergeAlternately(
                word1,
                word2,
            )
            == output
        )
