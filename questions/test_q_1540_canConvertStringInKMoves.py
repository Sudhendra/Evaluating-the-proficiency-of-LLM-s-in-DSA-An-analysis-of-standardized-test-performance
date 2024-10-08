import pytest
from q_1540_canConvertStringInKMoves import Solution


@pytest.mark.parametrize(
    "s, t, k, output",
    [("input", "ouput", 9, True), ("abc", "bcd", 10, False), ("aab", "bbb", 27, True)],
)
class TestSolution:
    def test_canConvertString(self, s: str, t: str, k: int, output: bool):
        sc = Solution()
        assert (
            sc.canConvertString(
                s,
                t,
                k,
            )
            == output
        )
