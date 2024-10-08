import pytest
from q_1505_minimumPossibleIntegerAfterAtMostKAdjacentSwapsOnDigits import Solution


@pytest.mark.parametrize(
    "num, k, output", [("4321", 4, "1342"), ("100", 1, "010"), ("36789", 1000, "36789")]
)
class TestSolution:
    def test_minInteger(self, num: str, k: int, output: str):
        sc = Solution()
        assert (
            sc.minInteger(
                num,
                k,
            )
            == output
        )
