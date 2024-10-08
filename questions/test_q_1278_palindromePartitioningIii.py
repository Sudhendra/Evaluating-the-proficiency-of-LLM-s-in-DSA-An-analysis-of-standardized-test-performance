import pytest
from q_1278_palindromePartitioningIii import Solution


@pytest.mark.parametrize(
    "s, k, output", [("abc", 2, 1), ("aabbc", 3, 0), ("leetcode", 8, 0)]
)
class TestSolution:
    def test_palindromePartition(self, s: str, k: int, output: int):
        sc = Solution()
        assert (
            sc.palindromePartition(
                s,
                k,
            )
            == output
        )
