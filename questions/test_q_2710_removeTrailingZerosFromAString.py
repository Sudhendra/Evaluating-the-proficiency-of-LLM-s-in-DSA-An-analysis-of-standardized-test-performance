import pytest
from q_2710_removeTrailingZerosFromAString import Solution


@pytest.mark.parametrize("num, output", [("51230100", "512301"), ("123", "123")])
class TestSolution:
    def test_removeTrailingZeros(self, num: str, output: str):
        sc = Solution()
        assert (
            sc.removeTrailingZeros(
                num,
            )
            == output
        )
