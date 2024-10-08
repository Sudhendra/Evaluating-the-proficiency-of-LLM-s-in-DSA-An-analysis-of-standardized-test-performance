import pytest
from q_0401_binaryWatch import Solution


@pytest.mark.parametrize(
    "turnedOn, output",
    [
        (
            1,
            [
                "0:01",
                "0:02",
                "0:04",
                "0:08",
                "0:16",
                "0:32",
                "1:00",
                "2:00",
                "4:00",
                "8:00",
            ],
        ),
        (9, []),
    ],
)
class TestSolution:
    def test_readBinaryWatch(self, turnedOn: int, output: List[str]):
        sc = Solution()
        assert (
            sc.readBinaryWatch(
                turnedOn,
            )
            == output
        )
