import pytest
from q_0854_kSimilarStrings import Solution


@pytest.mark.parametrize("s1, s2, output", [("ab", "ba", 1), ("abc", "bca", 2)])
class TestSolution:
    def test_kSimilarity(self, s1: str, s2: str, output: int):
        sc = Solution()
        assert (
            sc.kSimilarity(
                s1,
                s2,
            )
            == output
        )
