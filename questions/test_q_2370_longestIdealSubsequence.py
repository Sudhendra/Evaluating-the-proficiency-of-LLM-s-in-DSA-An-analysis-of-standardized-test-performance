import pytest
from q_2370_longestIdealSubsequence import Solution


@pytest.mark.parametrize("s, k, output", [("acfgbd", 2, 4), ("abcd", 3, 4)])
class TestSolution:
    def test_longestIdealString(self, s: str, k: int, output: int):
        sc = Solution()
        assert (
            sc.longestIdealString(
                s,
                k,
            )
            == output
        )
