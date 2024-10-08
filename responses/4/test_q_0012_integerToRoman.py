import pytest
from q_0012_integerToRoman import Solution


@pytest.mark.parametrize("num, output", [(3, "III"), (58, "LVIII"), (1994, "MCMXCIV")])
class TestSolution:
    def test_intToRoman(self, num: int, output: str):
        sc = Solution()
        assert (
            sc.intToRoman(
                num,
            )
            == output
        )
