import pytest
from q_2311_longestBinarySubsequenceLessThanOrEqualToK import Solution


@pytest.mark.parametrize("s, k, output", [("1001010", 5, 5), ("00101001", 1, 6)])
class TestSolution:
    def test_longestSubsequence(self, s: str, k: int, output: int):
        sc = Solution()
        assert (
            sc.longestSubsequence(
                s,
                k,
            )
            == output
        )
