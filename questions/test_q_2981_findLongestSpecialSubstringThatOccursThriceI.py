import pytest
from q_2981_findLongestSpecialSubstringThatOccursThriceI import Solution


@pytest.mark.parametrize("s, output", [("aaaa", 2), ("abcdef", -1), ("abcaba", 1)])
class TestSolution:
    def test_maximumLength(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.maximumLength(
                s,
            )
            == output
        )
