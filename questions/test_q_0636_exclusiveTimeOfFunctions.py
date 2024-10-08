import pytest
from q_0636_exclusiveTimeOfFunctions import Solution


@pytest.mark.parametrize(
    "n, logs, output",
    [
        (2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"], [3, 4]),
        (
            1,
            ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"],
            [8],
        ),
        (
            2,
            ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"],
            [7, 1],
        ),
    ],
)
class TestSolution:
    def test_exclusiveTime(self, n: int, logs: List[str], output: List[int]):
        sc = Solution()
        assert (
            sc.exclusiveTime(
                n,
                logs,
            )
            == output
        )
