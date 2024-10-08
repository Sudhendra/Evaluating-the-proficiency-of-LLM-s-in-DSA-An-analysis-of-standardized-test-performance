import pytest
from q_0013_romanToInteger import Solution


@pytest.mark.parametrize("s, output", [("III", 3), ("LVIII", 58), ("MCMXCIV", 1994)])
class TestSolution:
    def test_romanToInt(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.romanToInt(
                s,
            )
            == output
        )
