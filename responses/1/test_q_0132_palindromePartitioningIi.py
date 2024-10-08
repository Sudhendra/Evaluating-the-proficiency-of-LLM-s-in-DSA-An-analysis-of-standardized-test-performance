import pytest
from q_0132_palindromePartitioningIi import Solution


@pytest.mark.parametrize("s, output", [("aab", 1), ("a", 0), ("ab", 1)])
class TestSolution:
    def test_minCut(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.minCut(
                s,
            )
            == output
        )
