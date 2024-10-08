import pytest
from q_1147_longestChunkedPalindromeDecomposition import Solution


@pytest.mark.parametrize(
    "text, output",
    [
        ("ghiabcdefhelloadamhelloabcdefghi", 7),
        ("merchant", 1),
        ("antaprezatepzapreanta", 11),
    ],
)
class TestSolution:
    def test_longestDecomposition(self, text: str, output: int):
        sc = Solution()
        assert (
            sc.longestDecomposition(
                text,
            )
            == output
        )
