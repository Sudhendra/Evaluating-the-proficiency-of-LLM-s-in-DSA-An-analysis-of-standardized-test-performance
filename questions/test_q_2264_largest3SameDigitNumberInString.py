import pytest
from q_2264_largest3SameDigitNumberInString import Solution


@pytest.mark.parametrize(
    "num, output", [("6**777**133339", "777"), ("23**000**19", "000"), ("42352338", "")]
)
class TestSolution:
    def test_largestGoodInteger(self, num: str, output: str):
        sc = Solution()
        assert (
            sc.largestGoodInteger(
                num,
            )
            == output
        )
