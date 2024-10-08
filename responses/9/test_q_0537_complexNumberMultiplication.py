import pytest
from q_0537_complexNumberMultiplication import Solution


@pytest.mark.parametrize(
    "num1, num2, output", [("1+1i", "1+1i", "0+2i"), ("1+-1i", "1+-1i", "0+-2i")]
)
class TestSolution:
    def test_complexNumberMultiply(self, num1: str, num2: str, output: str):
        sc = Solution()
        assert (
            sc.complexNumberMultiply(
                num1,
                num2,
            )
            == output
        )
