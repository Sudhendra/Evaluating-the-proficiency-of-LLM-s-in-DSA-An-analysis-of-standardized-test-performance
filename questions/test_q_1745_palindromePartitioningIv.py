import pytest
from q_1745_palindromePartitioningIv import Solution


@pytest.mark.parametrize("s, output", [("abcbdd", True), ("bcbddxy", False)])
class TestSolution:
    def test_checkPartitioning(self, s: str, output: bool):
        sc = Solution()
        assert (
            sc.checkPartitioning(
                s,
            )
            == output
        )
