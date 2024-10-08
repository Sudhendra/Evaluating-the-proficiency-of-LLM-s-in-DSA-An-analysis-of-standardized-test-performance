import pytest
from q_1784_checkIfBinaryStringHasAtMostOneSegmentOfOnes import Solution


@pytest.mark.parametrize("s, output", [("1001", False), ("110", True)])
class TestSolution:
    def test_checkOnesSegment(self, s: str, output: bool):
        sc = Solution()
        assert (
            sc.checkOnesSegment(
                s,
            )
            == output
        )
