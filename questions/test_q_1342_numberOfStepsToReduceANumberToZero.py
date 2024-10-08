import pytest
from q_1342_numberOfStepsToReduceANumberToZero import Solution


@pytest.mark.parametrize("num, output", [(14, 6), (8, 4), (123, 12)])
class TestSolution:
    def test_numberOfSteps(self, num: int, output: int):
        sc = Solution()
        assert (
            sc.numberOfSteps(
                num,
            )
            == output
        )
