import pytest
from q_1694_reformatPhoneNumber import Solution


@pytest.mark.parametrize(
    "number, output",
    [
        ("1-23-45 6", "123-456"),
        ("123 4-567", "123-45-67"),
        ("123 4-5678", "123-456-78"),
    ],
)
class TestSolution:
    def test_reformatNumber(self, number: str, output: str):
        sc = Solution()
        assert (
            sc.reformatNumber(
                number,
            )
            == output
        )
