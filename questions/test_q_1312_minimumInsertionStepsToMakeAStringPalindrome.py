import pytest
from q_1312_minimumInsertionStepsToMakeAStringPalindrome import Solution


@pytest.mark.parametrize("s, output", [("zzazz", 0), ("mbadm", 2), ("leetcode", 5)])
class TestSolution:
    def test_minInsertions(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.minInsertions(
                s,
            )
            == output
        )
