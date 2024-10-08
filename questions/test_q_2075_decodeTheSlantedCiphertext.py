import pytest
from q_2075_decodeTheSlantedCiphertext import Solution


@pytest.mark.parametrize(
    "encodedText, rows, output",
    [
        ("ch   ie   pr", 3, "cipher"),
        ("iveo    eed   l te   olc", 4, "i love leetcode"),
        ("coding", 1, "coding"),
    ],
)
class TestSolution:
    def test_decodeCiphertext(self, encodedText: str, rows: int, output: str):
        sc = Solution()
        assert (
            sc.decodeCiphertext(
                encodedText,
                rows,
            )
            == output
        )
