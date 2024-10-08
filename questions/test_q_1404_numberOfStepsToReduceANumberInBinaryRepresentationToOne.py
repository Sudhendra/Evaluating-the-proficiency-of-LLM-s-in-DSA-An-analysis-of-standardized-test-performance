import pytest
from q_1404_numberOfStepsToReduceANumberInBinaryRepresentationToOne import Solution


@pytest.mark.parametrize("s, output", [("1101", 6), ("10", 1), ("1", 0)])
class TestSolution:
    def test_numSteps(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.numSteps(
                s,
            )
            == output
        )
