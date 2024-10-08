import pytest
from q_2120_executionOfAllSuffixInstructionsStayingInAGrid import Solution


@pytest.mark.parametrize(
    "n, startPos, s, output",
    [
        (3, [0, 1], "RRDDLU", [1, 5, 4, 3, 1, 0]),
        (2, [1, 1], "LURD", [4, 1, 0, 0]),
        (1, [0, 0], "LRUD", [0, 0, 0, 0]),
    ],
)
class TestSolution:
    def test_executeInstructions(
        self, n: int, startPos: List[int], s: str, output: List[int]
    ):
        sc = Solution()
        assert (
            sc.executeInstructions(
                n,
                startPos,
                s,
            )
            == output
        )
