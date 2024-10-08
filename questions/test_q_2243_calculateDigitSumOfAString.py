import pytest
from q_2243_calculateDigitSumOfAString import Solution


@pytest.mark.parametrize(
    "s, k, output", [("11111222223", 3, "135"), ("00000000", 3, "000")]
)
class TestSolution:
    def test_digitSum(self, s: str, k: int, output: str):
        sc = Solution()
        assert (
            sc.digitSum(
                s,
                k,
            )
            == output
        )
