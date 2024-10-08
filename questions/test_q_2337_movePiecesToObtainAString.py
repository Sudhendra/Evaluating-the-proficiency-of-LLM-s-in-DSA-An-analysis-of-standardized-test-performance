import pytest
from q_2337_movePiecesToObtainAString import Solution


@pytest.mark.parametrize(
    "start, target, output",
    [("_L__R__R_", "L______RR", True), ("R_L_", "__LR", False), ("_R", "R_", False)],
)
class TestSolution:
    def test_canChange(self, start: str, target: str, output: bool):
        sc = Solution()
        assert (
            sc.canChange(
                start,
                target,
            )
            == output
        )
