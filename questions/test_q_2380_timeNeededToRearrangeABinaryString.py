import pytest
from q_2380_timeNeededToRearrangeABinaryString import Solution


@pytest.mark.parametrize("s, output", [("0110101", 4), ("11100", 0)])
class TestSolution:
    def test_secondsToRemoveOccurrences(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.secondsToRemoveOccurrences(
                s,
            )
            == output
        )
