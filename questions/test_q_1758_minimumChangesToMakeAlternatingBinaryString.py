import pytest
from q_1758_minimumChangesToMakeAlternatingBinaryString import Solution


@pytest.mark.parametrize("s, output", [("0100", 1), ("10", 0), ("1111", 2)])
class TestSolution:
    def test_minOperations(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.minOperations(
                s,
            )
            == output
        )
