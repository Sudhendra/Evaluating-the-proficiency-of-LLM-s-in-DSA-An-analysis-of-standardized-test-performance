import pytest
from q_0273_integerToEnglishWords import Solution


@pytest.mark.parametrize(
    "num, output",
    [
        (123, "One Hundred Twenty Three"),
        (12345, "Twelve Thousand Three Hundred Forty Five"),
        (
            1234567,
            "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven",
        ),
    ],
)
class TestSolution:
    def test_numberToWords(self, num: int, output: str):
        sc = Solution()
        assert (
            sc.numberToWords(
                num,
            )
            == output
        )
